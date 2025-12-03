scores = []

filename = './input.txt'

with open(filename, 'r') as file:
    for line in file:
        values = list(map(int, line.split()))
        scores.append(values)

def is_safe(row):
    fin = True
    direction = 'down'

    for i, x in enumerate(row):
        if i == 1:
            if x > row[0]:
                direction = 'up'
            elif x < row[0]:
                direction = 'down'

        if i != 0:
            diff = abs(x - row[i - 1])
            if diff < 1 or diff > 3:
                fin = False
                break

            if x > row[i - 1] and direction == 'down':
                fin = False
                break
            elif x < row[i - 1] and direction == 'up':
                fin = False
                break
            elif x == row[i - 1]:
                fin = False
                break
    
    return fin

def solution_a():
    return sum([1 for x in scores if is_safe(x)])

def solution_b():
    fin = 0

    for xs in scores:
        if is_safe(xs):
            fin += 1
        else:
            omitted_safeties = map(lambda i: is_safe(xs[:i] + xs[i + 1:]), range(len(xs)))
            if sum([1 for x in omitted_safeties if x]) > 0:
                fin += 1

    return fin

print(f"Problem 1 answer: {solution_a()}")
print(f"Problem 2 answer: {solution_b()}")
