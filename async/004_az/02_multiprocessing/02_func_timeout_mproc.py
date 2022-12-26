# The problem
# Sometimes you may want to impose a timeout on a Python function. Why would you want to do such a thing? Let’s say you’re computing something but you know there are some hopeless scenarios where the computation just takes too long, and you’d be OK to just skip them and go on with the rest of the workflow.
#
# For an illustration, the figure below shows several tasks. Those that take longer than the specified timeout should be aborted (orange) and the remaining tasks that take a reasonable amount of time should be executed normally (green).

# Solution using the multiprocessing module
import multiprocessing as mp
import random
import time


def do_stuff(n):
    time.sleep(n)
    print('slept for {}s'.format(n))

# runs indefinitely. At each passage through the infinite loop, it randomly selects a duration between 1 and 5 seconds. It then spawns a new multiprocessing.Process that executes the time-consuming do_stuff() function for the random duration. If do_stuff() doesn’t finish in 3 seconds (actually, 3.01 seconds), the process terminates:
def main():
    max_duration = 3

    while True:
        duration = random.choice([x for x in range(1, 5)])
        print('duration = {}: '.format(duration), end='', flush=True)

        # do_stuff() run until it either completes or hits the 3-second mark,
        # whichever event comes first
        process = mp.Process(target=do_stuff, args=(duration,))
        process.start()

        # 1) use a non-integer timeout, not like in signal
        # 2) Although multiprocessing is the package that comes to mind when attempting to parallelize processes, its basic role is to simply spawn processes, as its name implies. (Processes spawned with multiprocessing may, but do not have to, be parallel.) We can set a timeout on the processes that are spawned, which is exactly what we are looking for here.
        # 3)  we actually specify the timeout. In other words, we wait for it to finish for the specified timeout.
        process.join(timeout=max_duration + 0.01)

        # we check whether the process actually finished, in which case is_alive() returns false. If it is still running, we terminate the process and display a message on STDOUT.
        if process.is_alive():
            process.terminate()
            process.join()
            print('took too long')

# duration = 3: slept for 3s
# duration = 4: took too long
# duration = 3: Process Process-4:

if __name__ == '__main__':
    main()

# 1) Simply spawning processes with the multiprocessing module does not mean we have parallelism. In order to do this we’d need to add tasks to a multiprocessing.Pool. This article or this one show examples of pools.
# 2) Care must be taken when using terminate() to stop a process. Here is what the Python documentation has to say about it:
# Warning: If this method is used when the associated process is using a pipe or queue then the pipe or queue is liable to become corrupted and may become unusable by other process [sic]. Similarly, if the process has acquired a lock or semaphore etc. then terminating it is liable to cause other processes to deadlock.