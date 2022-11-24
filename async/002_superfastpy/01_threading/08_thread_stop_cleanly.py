# Using a daemon thread is not a good idea
# The Python threading documentation explains that a thread may be started as a daemon, meaning that “the entire Python
# program exits when only daemon threads are left”. The main program itself is not a daemon thread.
# Note: Daemon threads are abruptly stopped at shutdown. Their resources (such as open files, database transactions, etc.)
# may not be released properly. If you want your threads to stop gracefully, make them non-daemonic and use a suitable
# signalling mechanism such as an Event.


# A clean thread exit using events and signals
# https://docs.python.org/3/library/threading.html#threading.Event
# Event is a simple object that can be set or cleared. It can be used to signal to the thread that it needs perform
# its cleanup and then stop.

# The idea is to use such an event here (let us call it a stop event). Initially not set, the stop event becomes set when a keyboard interrupt is received. The worker thread then breaks out from the loop if the stop event is set and performs its cleanup.
import threading

stop_event = threading.Event()


import signal
import threading
import time
import os

def send_ctrl_c(pid=None, time_sleep=2):
    time.sleep(time_sleep)
    pid = pid or os.getpid()
    if hasattr(signal, 'CTRL_C_EVENT'):
        # windows. Need CTRL_C_EVENT to raise the signal in the whole process group
        os.kill(pid, signal.CTRL_C_EVENT)
    else:
        # unix
        os.kill(pid, signal.SIGINT)


def do_some_work(n_iter):
    for i in range(n_iter):

        # break in case ctr-c
        # The worker thread then breaks out from the loop if the stop event is set and performs its cleanup.
        if stop_event.is_set():
            break

        print(f'iteration {i + 1}/{n_iter}')
        time.sleep(0.5)

    # Notice that when the thread is stopped it now finally gets to the print('Thread done') line (a placeholder for an actual cleanup task)
    # Moreover, the main program also gets to the print('Program done') line.
    print('Thread done')


# The idea is to use such an event here (let us call it a stop event). Initially not set,
#  must have two arguments, the signal and the frame, even though the second argument is not used:
def handle_kb_interrupt(sig, frame):
    stop_event.set()

# Clean exit from a thread can therefore be achieved using a threading event and a signal handler.
if __name__ == '__main__':
    # threading Event is a simple object that can be set or cleared. It can be used to signal to the thread that it needs perform its cleanup and then stop.
    stop_event = threading.Event()

    # the stop event becomes set when a keyboard interrupt is received.
    # The stop event needs to be set when a keyboard interrupt is intercepted. This is done by registering the SIGINT signal with a handler function.
    # https://en.wikipedia.org/wiki/Signal_(IPC)
    signal.signal(signal.SIGINT, handle_kb_interrupt)

    n_iter = 10
    thread = threading.Thread(target=do_some_work, args=(n_iter,))

    thread.start()
    send_ctrl_c()

    thread.join()
    print('Program done')