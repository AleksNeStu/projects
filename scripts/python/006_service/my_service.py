# Running a Python script as a systemd service
# An executable can be made into a systemd service by creating a unit (configuration) file, also known as a .service file (see the systemd.service man page). The .service files are stored in a specific location and have a certain format.

# There are actually three places where unit files may be stored:
#
# /etc/systemd/system/: system-specific; take precedence over run-time unit files
# /run/systemd/system/: run-time; take precedence over default unit files
# /usr/lib/systemd/system/: default; may be overwritten when the system updates
# If you create your own systemd service, place the .service unit file in /etc/systemd/system/.


# Recall the original assumption: my_service.py opens file descriptors and uses the underlying resources. Whenever the service stops running (through sudo systemctl stop my-service.service, for example), it must do so gracefully by closing the open resources first.
#
# Before diving into the possible solutions, let us first take a look at the general structure of the my_service.py script.


# The Python service (my_service.py) may be a TCP server, client, or any other process that needs to run as a daemon. For the purpose of this example, let us suppose that the service uses a standard event loop and opens a named pipe in /tmp to read from it. Instead of doing something useful, our example service will just sleep and then log something when it wakes up. The general structure is as follows (possible exceptions from the os module are not caught for brevity purposes):

import logging
import os
import sys
import time


class MyService:
    FIFO = '/tmp/myservice_pipe'

    def __init__(self, delay=5):
        self.logger = self._init_logger()
        self.delay = delay
        if not os.path.exists(MyService.FIFO):
            os.mkfifo(MyService.FIFO)
        self.fifo = os.open(MyService.FIFO, os.O_RDWR | os.O_NONBLOCK)
        self.logger.info('MyService instance created')

    def _init_logger(self):
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.DEBUG)
        stdout_handler = logging.StreamHandler()
        stdout_handler.setLevel(logging.DEBUG)
        stdout_handler.setFormatter(logging.Formatter('%(levelname)8s | %(message)s'))
        logger.addHandler(stdout_handler)
        return logger

    def start(self):
        try:
            while True:
                time.sleep(self.delay)
                self.logger.info('Tick')
        except KeyboardInterrupt:
            self.logger.warning('Keyboard interrupt (SIGINT) received...')
            self.stop()

    def stop(self):
        self.logger.info('Cleaning up...')
        if os.path.exists(MyService.FIFO):
            os.close(self.fifo)
            os.remove(MyService.FIFO)
            self.logger.info('Named pipe removed')
        else:
            self.logger.error('Named pipe not found, nothing to clean up')
        sys.exit(0)

    def _handle_sigterm(self, sig, frame):
        # Note the two arguments sig and frame: although not used explicitly, they must be present because this is the method that we will register for handling SIGTERM. If they are absent we get a TypeError when a SIGTERM is received. We add the following line to the __init__() method:
        self.logger.warning('SIGTERM received...')
        self.stop()
        # If we check the system log with journalctl -u my-service.service we see the following:


# Conclusion
# That’s it! You can now use either of the two methods to stop your Python systemd service gracefully: either tell systemd to kill it with a SIGINT or, better yet, install a custom SIGTERM handler.
#
# There’s a caveat with both approaches if the service launches more than one process. The systemd.kill man page explains that by default (when KillMode=control-group) all the processes launched by the unit file will receive SIGTERM (or SIGINT if we use KillSignal=SIGINT as explained here). However, if they fail to stop, they will be knocked-out with SIGKILL. In such situations, one should be extra-careful with proper shutdown and cleanup.

if __name__ == '__main__':
    service = MyService()
    service.start()

# How to stop the Python service gracefully
# In the previous section we’ve seen that the named pipe is removed as expected if my_service.py is executed in a console. However, if we run it as a systemd service, stopping it via systemctl will result in an improper shutdown of our service: the named pipe is not removed :scream:
#
# This happens because, by default, the kill signal sent by systemd when using systemctl stop is SIGTERM, not SIGINT, therefore we cannot catch it as a KeyboardInterrupt.
#
# Here are two solutions for this problem.

# 1) Use SIGINT instead of SIGTERM
# The most immediate solution is to instruct systemd to send a SIGINT (registered as a keyboard interrupt) instead of the default SIGTERM. This is done by adding the following line to the [Service] section of the my-service.service unit file:

# KillSignal=SIGINT

# This way, whenever we stop or restart the service with systemctl, the signal sent to kill my_service.py is SIGINT and it is caught by the except block in lines 32-34.

# 2) Use a SIGTERM handler
# The other solution is to register a signal handler for SIGTERM. For this, we will need to import signal and instruct Python to do something useful when receiving a SIGTERM. We add the following method to the MyService class: