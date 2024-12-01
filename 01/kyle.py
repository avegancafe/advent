from functools import reduce
from collections import Counter


filename = 'input.txt'

x = []
y = []

with open(filename, 'r') as file:
    for line in file:
        values = list(map(int, line.split()))
        x.append(values[0])
        y.append(values[1])

x.sort()
y.sort()

zipped = list(zip(x, y))

def problem_a():
    def calculate_final(agg, input):
        x, y = input
        return agg + abs(x - y)

    return reduce(calculate_final, zipped, 0)

def problem_b():
    y_counter = Counter(y)

    return sum([y_counter[i] * i for i in x])

def efficient_solution():
    """
    This solution is O(n log(n)) because of the sorting of the x and y arrays.
    This specific part of the algorithm is O(n) because it iterates over the
    zipped array once.
    """
    y_counter = {}
    solution_a = 0

    for i, j in zipped:
        y_counter[j] = y_counter.get(j, 0) + 1
        solution_a += abs(i - j)

    solution_b = sum([y_counter.get(i, 0) * i for i in x])

    print(f"Problem 1 answer: {solution_a}")
    print(f"Problem 2 answer: {solution_b}")

print(f"Problem 1 answer: {problem_a()}")
print(f"Problem 2 answer: {problem_b()}")
print("Efficient solution:")
efficient_solution()
