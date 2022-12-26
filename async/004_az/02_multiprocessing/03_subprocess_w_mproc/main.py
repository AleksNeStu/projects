import subprocess
import multiprocessing as mp
from tqdm import tqdm


NUMBER_OF_TASKS = 4
progress_bar = tqdm(total=NUMBER_OF_TASKS)


def work(sec_sleep):
    command = ['python', 'worker.py', sec_sleep]
    subprocess.call(command)


def update_progress_bar(_):
    progress_bar.update()


if __name__ == '__main__':
    pool = mp.Pool(NUMBER_OF_TASKS)

    for seconds in [str(x) for x in range(1, NUMBER_OF_TASKS + 1)]:
        pool.apply_async(work, (seconds,), callback=update_progress_bar)

    pool.close()
    pool.join()