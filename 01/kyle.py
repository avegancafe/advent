from functools import reduce

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

def calculate_final(agg, input):
    x, y = input
    return agg + abs(x - y)

final = reduce(calculate_final, zipped, 0)

print(final)
