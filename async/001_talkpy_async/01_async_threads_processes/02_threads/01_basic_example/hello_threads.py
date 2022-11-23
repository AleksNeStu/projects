import threading
import time


def main():
    threads = [
        threading.Thread(name="Michael", target=greeter, args=("Michael", 10), daemon=True),
        threading.Thread(name="Sarah", target=greeter, args=("Sarah", 5), daemon=True),
        threading.Thread(name="Zoe", target=greeter, args=("Zoe", 2), daemon=True),
        threading.Thread(name="Mark", target=greeter, args=("Mark", 11), daemon=True),
    ]

    [t.start() for t in threads]

    print("This is other work.")
    print(2 * 2)

    [t.join(timeout=2) for t in threads]

    print("Done.")


def greeter(name: str, times: int):
    for n in range(0, times):
        print(f"{n}. Hello there {name}")
        time.sleep(1)


if __name__ == '__main__':
    main()
