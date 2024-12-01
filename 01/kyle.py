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

print(f"Problem 1 answer: {problem_a()}")
print(f"Problem 2 answer: {problem_b()}")
