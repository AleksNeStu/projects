import sys
import time
import os


def do_work(n):
    time.sleep(n)
    print(f'I just did some hard work for {n}s!, pid: {os.getpid()}')


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Please provide one integer argument', file=sys.stderr)
        exit(1)
    try:
        seconds = int(sys.argv[1])
        do_work(seconds)
    except Exception as e:
        print(e)

# The shared resource
# Here is where the shared resource come into play. At the end of each “computation”, the worker process accesses this shared resource in both read and write mode. For the purpose of this example, let us imagine the shared resource is a list of results. The worker process needs to read the resource and update it with a certain value only if the value is not yet present in the list.