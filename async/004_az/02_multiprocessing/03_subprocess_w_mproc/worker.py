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