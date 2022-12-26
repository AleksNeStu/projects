import threading


counter = 0

def increment(n):
    global counter
    for _ in range(n):
        counter += 1


def main():
    thr1 = threading.Thread(target=increment, args=(500000,))
    thr2 = threading.Thread(target=increment, args=(500000,))

    thr1.start()
    thr2.start()

    thr1.join()
    thr2.join()

    print(f'counter = {counter}')


if __name__ == '__main__':
    main()