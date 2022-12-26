import threading
import time


def my_task(x, y):
    print('{} got x={}, y={}'.format(threading.current_thread().name, x, y))
    time.sleep(x + y)
    print('{} finished after {:.2f} seconds'.format(
        threading.current_thread().name, x + y))


def main():
    # thr1 = threading.Thread(target=my_task, name='Thread 1', args=(1, 2,))
    thr1 = threading.Thread(target=my_task, args=(1, 2,))
    thr2 = threading.Thread(target=my_task, args=(.1, .2,))

    thr1.start()
    thr2.start()

    thr1.join()
    thr2.join()

    print('Main thread finished')


if __name__ == '__main__':
    main()