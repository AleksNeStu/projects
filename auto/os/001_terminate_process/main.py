import os
import signal

# What is Ctrl-C in bash?
# When you hit Ctrl + c , the line discipline of your terminal sends SIGINT to processes in the foreground process group. Bash, when job control is disabled, runs everything in the same process group as the bash process itself. Job control is disabled by default when Bash interprets a script.02-Jun-2021
#
# What is SIGUSR1 in Python?
# 10 (SIGUSR1): user-defined signal. 11 (SIGSEGV): segmentation fault due to illegal access of a memory segment. 12 (SIGUSR2): user-defined signal. 13 (SIGPIPE): writing into a pipe, and nobody is reading from it. 14 (SIGALRM): the timer terminated (alarm)30-Nov-2018
# What is Sigkill in Python?
# SIGKILL is where the Python process is terminated by your system. Reasons I have seen this: Low resources (not enough RAM, usually) - monitor and see how much the program is using. You might also want to try explicitly setting n_jobs to a low number, as CPU over-subscription could be an issue.11-Aug-2021
#
# How do I use Ctrl-C in Linux?
# While in a command line such as MS-DOS, Linux, and Unix, Ctrl + C is used to send a SIGINT signal, which cancels or terminates the currently-running program. For example, if a script or program is frozen or stuck in an infinite loop, pressing Ctrl + C cancels that command and returns you to the command line.13-Mar-2021
#
# How do you Ctrl D in shell script?
# In the Linux command-line shell, pressing Ctrl + D logs out of the interface. If you used the sudo command to execute commands as another user, pressing Ctrl + D exits out of that other user and puts you back as the user you originally logged into.31-Dec-2020
#
# How do you write Ctrl Z in shell script?
# The Ctrl+Z keys generate a SIGTSTP signal to stop any processes running in the shell, and that leaves the program in memory. The number between brackets, which is (1), is the job number. If you try to exit the shell and you have a stopped job assigned to your shell, the bash warns you if you.15-Feb-2017

# ex 0
def send_ctrl_c(pid=None):
    pid = pid or os.getpid()
    if hasattr(signal, 'CTRL_C_EVENT'):
        # windows. Need CTRL_C_EVENT to raise the signal in the whole process group
        os.kill(pid, signal.CTRL_C_EVENT)
    else:
        # unix
        os.kill(pid, signal.SIGINT)

# ex1
def raise_sigint():
    """
    Raising the SIGINT signal in the current process and all sub-processes.

    os.kill() only issues a signal in the current process (without subprocesses).
    CTRL+C on the console sends the signal to the process group (which we need).
    """
    if hasattr(signal, 'CTRL_C_EVENT'):
        # windows. Need CTRL_C_EVENT to raise the signal in the whole process group
        os.kill(os.getpid(), signal.CTRL_C_EVENT)
    else:
        # unix.
        pgid = os.getpgid(os.getpid())
        if pgid == 1:
            os.kill(os.getpid(), signal.SIGINT)
        else:
            os.killpg(os.getpgid(os.getpid()), signal.SIGINT)



# ex2
def test_CTRL_C_EVENT(self):
    from ctypes import wintypes
    import ctypes

    # Make a NULL value by creating a pointer with no argument.
    NULL = ctypes.POINTER(ctypes.c_int)()
    SetConsoleCtrlHandler = ctypes.windll.kernel32.SetConsoleCtrlHandler
    SetConsoleCtrlHandler.argtypes = (ctypes.POINTER(ctypes.c_int),
                                      wintypes.BOOL)
    SetConsoleCtrlHandler.restype = wintypes.BOOL

    # Calling this with NULL and FALSE causes the calling process to
    # handle Ctrl+C, rather than ignore it. This property is inherited
    # by subprocesses.
    SetConsoleCtrlHandler(NULL, 0)

    self._kill_with_event(signal.CTRL_C_EVENT, "CTRL_C_EVENT")
