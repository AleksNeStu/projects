import datetime
import math
import multiprocessing

CONST = 30_000_000_0

def main():
    do_math(1)

    t0 = datetime.datetime.now()

    print(f"Doing math on {multiprocessing.cpu_count():,} processors.")

    pool = multiprocessing.Pool()
    processor_count = multiprocessing.cpu_count()
    tasks = []
    for n in range(1, processor_count + 1):
        task = pool.apply_async(do_math, (CONST * (n - 1) / processor_count,
                                          CONST * n / processor_count))
        tasks.append(task)

    pool.close()
    pool.join()

    dt = datetime.datetime.now() - t0
    print(f"Done in {dt.total_seconds():,.2f} sec.")
    print("Our results: ")
    for t in tasks:
        print(t.get())


def do_math(start=0, num=10):
    pos = start
    k_sq = 1000 * 1000
    ave = 0
    while pos < num:
        pos += 1
        val = math.sqrt((pos - k_sq) * (pos - k_sq))
        ave += val / num

    # print(int(ave))

    return int(ave)


if __name__ == '__main__':
    main()
