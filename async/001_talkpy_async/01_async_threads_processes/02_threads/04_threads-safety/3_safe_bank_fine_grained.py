# Fix global lock for entire process
import datetime
import random
import time
from threading import Thread, RLock
from typing import List


class Account:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance
        self.lock = RLock()


def main():
    accounts = create_accounts()
    total = sum(a.balance for a in accounts)

    validate_bank(accounts, total)
    print("Starting transfers...")

    jobs = [
        Thread(target=do_bank_stuff, args=(accounts, total)),
        Thread(target=do_bank_stuff, args=(accounts, total)),
        Thread(target=do_bank_stuff, args=(accounts, total)),
        Thread(target=do_bank_stuff, args=(accounts, total)),
        Thread(target=do_bank_stuff, args=(accounts, total)),
    ]

    t0 = datetime.datetime.now()

    [j.start() for j in jobs]
    [j.join() for j in jobs]

    dt = datetime.datetime.now() - t0

    print(f"Transfers complete ({dt.total_seconds():,.2f}) sec")
    validate_bank(accounts, total)


def do_bank_stuff(accounts, total):
    for num in range(1, 10_000 + 1):
        a1, a2 = get_two_accounts(accounts)
        amount = random.randint(1, 100)
        do_transfer(a1, a2, amount, num)
        validate_bank(accounts, total, quiet=True)


def create_accounts() -> List[Account]:
    return [
        Account(name='ac1', balance=5000),
        Account(name='ac2', balance=10000),
        Account(name='ac3', balance=7500),
        Account(name='ac4', balance=7000),
        Account(name='ac5', balance=6000),
        Account(name='ac6', balance=9000),
    ]


def do_transfer(from_account: Account, to_account: Account, amount: int, num_op: int):
    print(f"Num: {num_op}, from {from_account.name} to {to_account.name}, money: {amount}\n")
    if from_account.balance < amount:
        return

    # To avoid deadlock (make locks in the same order)
    lock1, lock2 = (
        (from_account.lock, to_account.lock)
        if id(from_account) < id(to_account)
        else (to_account.lock, from_account.lock)
    )

    with lock1:
        with lock2:
            from_account.balance -= amount
            time.sleep(.000)
            to_account.balance += amount


# transfer_lock = RLock()
#
# # from previous example
# def do_transfer_global_style(
#         from_account: Account, to_account: Account, amount: int):
#     if from_account.balance < amount:
#         return
#
#     with transfer_lock:
#         from_account.balance -= amount
#         time.sleep(.000)
#         to_account.balance += amount


def validate_bank(accounts: List[Account], total: int, quiet=False):
    # with transfer_lock:
    #     current = sum(a.balance for a in accounts)

    [a.lock.acquire() for a in sorted(accounts, key=lambda x: id(x))]
    current = sum(a.balance for a in accounts)
    [a.lock.release() for a in accounts]

    if current != total:
        print("ERROR: Inconsistent account balance: ${:,} vs ${:,}".format(
            current, total
        ), flush=True)
    elif not quiet:
        print(f"All good: Consistent account balance: ${total:,}", flush=True)


def get_two_accounts(accounts):
    a1 = random.choice(accounts)
    a2 = a1
    while a2 == a1:
        a2 = random.choice(accounts)

    return a1, a2


if __name__ == '__main__':
    main()
