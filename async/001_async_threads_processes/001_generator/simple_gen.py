from typing import List


def fib_func(n: int) -> List[int]:
    numbers = []
    current, nxt = 0, 1
    while len(numbers) < n:
        current, nxt = nxt, current + nxt
        numbers.append(current)

    return numbers

def fib_gen():
    current, nxt = 0, 1
    while True:
        current, nxt = nxt, current + nxt
        yield current


result = fib_gen()

for n in result:
    print(n, end=', ')
    if n > 10000:
        break

print()
print("Done")
