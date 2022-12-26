# import subprocess
#
# cmd = ['/path/to/cmd', 'arg1', 'arg2']  # the external command to run
# timeout_s = 10  # how many seconds to wait
#
# try:
#     p = subprocess.run(cmd, timeout=timeout_s)
# except subprocess.TimeoutExpired:
#     print(f'Timeout for {cmd} ({timeout_s}s) expired')




# Stopping a subprocess and its children on timeout
# The situation gets more complicated when the external command may launch one or several child processes. In order to be able to stop the child processes as well as the parent, it is necessary to use the Popen constructor.

# 3.296 Process Group - A collection of processes that permits the signaling of related processes. Each process in the system is a member of a process group that is identified by a process group ID. A newly created process joins the process group of its creator.
#
# 3.343 Session - A collection of process groups established for job control purposes. Each process group is a member of a session. A process is considered to be a member of the session of which its process group is a member. A newly created process joins the session of its creator. A process can alter its session membership; see setsid(). There can be multiple process groups in the same session.

# Popen() states the following:
#
# Warning: The preexec_fn parameter is not safe to use in the presence of threads in your application. The child process could deadlock before exec is called. If you must use it, keep it trivial! Minimize the number of libraries you call into.


import os
import signal
import subprocess
import sys

cmd = ['/path/to/cmd', 'arg1', 'arg2']  # the external command to run
timeout_s = 10  # how many seconds to wait

try:
    p = subprocess.Popen(cmd, start_new_session=True)
    p.wait(timeout=timeout_s)
except subprocess.TimeoutExpired:
    print(f'Timeout for {cmd} ({timeout_s}s) expired', file=sys.stderr)
    print('Terminating the whole process group...', file=sys.stderr)
    os.killpg(os.getpgid(p.pid), signal.SIGTERM)