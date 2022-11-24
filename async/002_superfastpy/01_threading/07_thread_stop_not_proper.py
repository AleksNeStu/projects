# Suppose a Python thread needs to be stopped cleanly (it might need to perform cleanup).

# For illustration, we will take a very simple program in with a single “worker” thread that displays a message when it
# is done. The message is a placeholder for real cleanup, and the thread itself sleeps for a given number of iterations
# (as a placeholder for significant work). In example, we want to stop the thread through a keyboard interrupt (Ctrl + C).

# By default, the thread is not stopped cleanly

import os
import signal
import threading
import time


# 1) The program can be stopped by hitting Ctrl + C, but the thread keeps running.
def do_some_work(n_iter):
    for i in range(n_iter):
        print(f'iteration {i + 1}/{n_iter}')
        time.sleep(0.5)
    print('Thread done')

def send_ctrl_c(pid=None):
    pid = pid or os.getpid()
    if hasattr(signal, 'CTRL_C_EVENT'):
        # windows. Need CTRL_C_EVENT to raise the signal in the whole process group
        os.kill(pid, signal.CTRL_C_EVENT)
    else:
        # unix
        os.kill(pid, signal.SIGINT)


# ~/projects/.venv/bin/python ~/.local/share/JetBrains/IntelliJIdea/python/helpers/pydev/pydevd.py --multiprocess
# --qt-support=auto --client 127.0.0.1 --port 33495 --file ~/Projects/projects/async/002_superfastpy/01_threading/07_thread_stop_cleanly.py
if __name__ == '__main__':
    n_iter = 20
    thread = threading.Thread(target=do_some_work, args=(n_iter,))
    thread.start()


    # The first Ctrl + C stops the main program, but not the thread. The second time, the thread is stopped as well.
    send_ctrl_c()
    # Traceback (most recent call last):
    #   File "~/projects/async/002_superfastpy/01_threading/07_thread_stop_cleanly.py", line 37, in <module>
    #     send_ctrl_c()
    #   File "~/projects/async/002_superfastpy/01_threading/07_thread_stop_cleanly.py", line 28, in send_ctrl_c
    #     os.kill(pid, signal.SIGINT)
    # KeyboardInterrupt
    # iteration 1/20


    thread.join()
    print('Program done')

# 2) Using a daemon thread is not a good idea
# The Python threading documentation explains that a thread may be started as a daemon, meaning that “the entire Python
# program exits when only daemon threads are left”. The main program itself is not a daemon thread.
# Note: Daemon threads are abruptly stopped at shutdown. Their resources (such as open files, database transactions, etc.)
# may not be released properly. If you want your threads to stop gracefully, make them non-daemonic and use a suitable
# signalling mechanism such as an Event.


# 3) A clean thread exit using events and signals
# https://docs.python.org/3/library/threading.html#threading.Event
# Event is a simple object that can be set or cleared. It can be used to signal to the thread that it needs perform
# its cleanup and then stop.

# The idea is to use such an event here (let us call it a stop event). Initially not set, the stop event becomes set when a keyboard interrupt is received. The worker thread then breaks out from the loop if the stop event is set and performs its cleanup.

stop_event = threading.Event()
