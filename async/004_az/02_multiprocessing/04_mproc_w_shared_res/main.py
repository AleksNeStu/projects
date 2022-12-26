import subprocess
import multiprocessing as mp
from tqdm import tqdm

NUMBER_OF_TASKS = 20
progress_bar = tqdm(total=NUMBER_OF_TASKS)


def work(sec_sleep, processed_values, lock):
    seconds = int(sec_sleep) % 10 + 1
    command = ['python', 'worker.py', str(seconds)]
    subprocess.call(command)
    with lock:
        if seconds not in processed_values:
            processed_values.append(seconds)


def update_progress_bar(_):
    progress_bar.update()


if __name__ == '__main__':
    tasks = [str(x) for x in range(1, NUMBER_OF_TASKS + 1)]
    pool = mp.Pool()
    manager = mp.Manager()
    lock = manager.Lock()
    shared_list = manager.list()

    for i in tasks:
        pool.apply_async(work, (i, shared_list, lock,),
                         callback=update_progress_bar)
    pool.close()
    pool.join()

    print(shared_list)


# What we will be doing now is launching 100 processes in parallel on as many threads as we have CPUs. Each process launches worker.py as a Python subprocess. As we have seen above, the worker script sleeps for a given number of seconds.

# This is only an example meant to show that we need to reserve exclusive access to a resource in both read and write mode if what we write into the shared resource is dependent on what the shared resource already contains.