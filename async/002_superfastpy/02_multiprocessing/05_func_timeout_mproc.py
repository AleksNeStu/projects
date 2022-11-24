# The problem
# Sometimes you may want to impose a timeout on a Python function. Why would you want to do such a thing? Let’s say you’re computing something but you know there are some hopeless scenarios where the computation just takes too long, and you’d be OK to just skip them and go on with the rest of the workflow.
#
# For an illustration, the figure below shows several tasks. Those that take longer than the specified timeout should be aborted (orange) and the remaining tasks that take a reasonable amount of time should be executed normally (green).


import multiprocessing
import random
import time


def do_stuff(n):
    time.sleep(n)
    print('slept for {}s'.format(n))


def main():
    max_duration = 2

    while True:
        duration = random.choice([x for x in range(1, 4)])
        print('duration = {}: '.format(duration), end='', flush=True)

        process = multiprocessing.Process(target=do_stuff, args=(duration,))
        process.start()
        process.join(timeout=max_duration + 0.01)

        if process.is_alive():
            process.terminate()
            process.join()
            print('took too long')


if __name__ == '__main__':
    main()