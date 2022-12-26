# The problem
# Sometimes you may want to impose a timeout on a Python function. Why would you want to do such a thing? Let’s say you’re computing something but you know there are some hopeless scenarios where the computation just takes too long, and you’d be OK to just skip them and go on with the rest of the workflow.
#
# For an illustration, the figure below shows several tasks. Those that take longer than the specified timeout should be aborted (orange) and the remaining tasks that take a reasonable amount of time should be executed normally (green).

# Solution using the signal module
# What are signals?
# Signals are a form of inter-process communication that only applies to POSIX-compliant operating systems. Note that Microsoft Windows is not POSIX-compliant, so this solution cannot be used when running Python on Windows.

# What are signals?
# Signals are a form of inter-process communication that only applies to POSIX-compliant operating systems. Note that Microsoft Windows is not POSIX-compliant, so this solution cannot be used when running Python on Windows.
#
# Signals can be regarded as software interrupts sent from the kernel to a process in order to inform it that a special event took place. The process receiving the signal can choose to handle it in a specific way (if the program was written with this intention, that is). Otherwise, signals are handled in a default manner specified by the default signal handlers. For example, when you press Ctrl + C in your Linux terminal to stop a running program, you are in fact sending it the SIGINT signal. The default handler for SIGINT is to stop process execution.
#
# Check out this article for more information on handling UNIX signals in Python.
# https://stackabuse.com/handling-unix-signals-in-python/


# import signal
# import time
#
# #  sometimes be very time-consuming
# def do_stuff(n):
#     time.sleep(n)
#     print('slept for {}s'.format(n))
#
#
# def main():
#     print('start')
#     signal.alarm(4)
#     do_stuff(2)
#     do_stuff(5)
#     do_stuff(6)
#     print('done')
#     # start
#     # slept for 2s
#     #
#     # Process finished with exit code 142 (interrupted by signal 14: SIGALRM)
#
#
# if __name__ == '__main__':
#     main()



# Next, we will define a handler for SIGALRM. A handler is a function that “handles a signal” in the specific way we instruct it to behave. User-defined handlers are used to override the default signal handlers. For example, suppose you want your program to ask the user to confirm her desire to quit the program when she presses Ctrl + C in the terminal. In this case you’d need a SIGINT handler that only exits upon confirmation. Note that signal handlers must respect a fixed prototype. To quote from the Python documentation:


# The handler is called with two arguments: the signal number and the current stack frame (…).

import sys
import random
import signal
import time


def handle_sigint(sig, frame):
    print('SIGINT received, terminating.')
    sys.exit()

# We catch that TimeoutError and continue execution until hitting Ctrl + C. As an added bonus, we also include a handler for SIGINT (Ctrl + C).
def handle_timeout(sig, frame):
    raise TimeoutError('took too long')


def do_stuff(n):
    time.sleep(n)



def main():
    signal.signal(signal.SIGINT, handle_sigint)
    # This handler only makes sense if it is registered for SIGALRM. Registering handle_timeout() for SIGALRM should be added to the main() function of the script above. Here is how to do it:
    signal.signal(signal.SIGALRM, handle_timeout)

    max_duration = 2

    #  loops indefinitely and at each iteration through the loop it attempts to do_stuff() for a random number of seconds between 1 and 10.
    while True:
        try:
            duration = random.choice([x for x in range(1, 4)])
            print(f"duration = {duration}: , max={max_duration} ", end='', flush=True)
            #  If do_stuff() is called with 2 seconds or more, then SIGALRM is sent and handled by raising a TimeoutError.

            #  let it run just below 6 seconds, because the argument to signal.alarm() is necessarily an integer. If that argument was 5, do_stuff() would not have been allowed to run for 5 seconds.
            signal.alarm(max_duration + 1)  # start waiting

            do_stuff(duration)
            signal.alarm(0)  # reset the alarm after each call to do_stuff()

        # handle_timeout
        except TimeoutError as exc:
            print('{}: {}'.format(exc.__class__.__name__, exc))
        else:
            print('slept for {}s'.format(duration))

# duration = 1: , max=2 slept for 1s
# duration = 3: , max=2 TimeoutError: took too long
# duration = 2: , max=2 slept for 2s
# duration = 3: , max=2 TimeoutError: took too long
# duration = 1: , max=2 slept for 1s
# duration = 2: , max=2 slept for 2s
# duration = 2: , max=2 slept for 2s
# duration = 3: , max=2 TimeoutError: took too long
# duration = 3: , max=2 SIGINT received, terminating.
#
# Process finished with exit code 0


# So how does the execution continue past the first timeout? As we’ve seen above, we installed a handler for SIGALRM (lines 12-13 and 22) that raises a TimeoutError. Exception handling is performed in the main() function inside an infinite loop (lines 26-36). If do_stuff() succeeds, the script displays a message informing the user for how long the function ran (lines 35-36). If the TimeoutError is caught, it is simply displayed and the script continues.

if __name__ == '__main__':
    main()


# Drawbacks
# Well, it works but there are two problems with this solution:
#
# As mentioned in the introduction to signals, this mechanism is only present on UNIX-like systems. If the script needs to run in a classic Windows environment, the signal module is not suitable.
# A SIGALRM can arrive at any time; however, its handler may only be ran between atomic instructions. By definition, atomic instructions cannot be interrupted. So if the timer runs out during such an operation, even though SIGALRM is sent, it won’t be handled until that long computation you’ve been trying to abort finally completes. Typically, when using external libraries implemented in pure C for performing long computations, the handling of SIGALRM may be delayed.

# Conclusion
# In this post we’ve seen a simple solution involving UNIX signals that may be used in some situations to set a timeout on a Python function. However, this solution is less than ideal for two reasons: the operating system must be POSIX-compliant and it can only work between atomic operations. In the next post we will examine a better solution using the multiprocessing module.

# https://stackabuse.com/handling-unix-signals-in-python/