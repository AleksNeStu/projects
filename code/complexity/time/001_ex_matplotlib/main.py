"""Complex algorithm with complexity calculation example."""

# - Write a function that return least integer that is not present in a
# given list and can not be represented by the summation of the sub-elements
# of the list.
# - Evaluate time code complexity using Big O notation

def set_w_nested_loop(input):
    import itertools

    sums = set()
    for idx in range(0, len(input) + 1):
        sums.update([sum(comb) for comb in itertools.combinations(input, idx)])

    for every in range(0, max(sums) + 2):
        if every not in input and every not in sums:
            return every


assert set_w_nested_loop([1, 2, 5, 7]) == 4
assert set_w_nested_loop([1, 2, 2, 5, 7]) == 18


# Calculate code complexity the solution from the task2
import random
import time

import matplotlib.pyplot as plt

def draw_time_complexity(func, max_len, max_elem):
    lengths_nested = []
    times_nested = []

    for length in range(0, max_len, 1):
        input = [random.randint(0, max_elem) for _ in range(length)]
        print(f"Input: {input}")

        # Time execution for nested lists version
        start = time.perf_counter()
        res = func(input)
        print(f"Result: {res}")
        end = time.perf_counter()

        # Store results
        lengths_nested.append(length)
        times_nested.append(end - start)


    # Plot results
    plt.style.use("dark_background")
    plt.figure().canvas.manager.set_window_title("Time Complexity")
    plt.xlabel("List Length")
    plt.ylabel("Execution Time (s)")
    plt.plot(lengths_nested, times_nested, label="set_w_nested_loop()")
    plt.legend()
    plt.tight_layout()
    plt.show()


draw_time_complexity(func=set_w_nested_loop, max_len=20, max_elem=99)