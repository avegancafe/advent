from functools import cmp_to_key

rules = {}
updates = []

reading_rules = True
with open("./input.txt") as file:
    for line in file:
        line = line.strip()

        if line == "":
            reading_rules = False
            continue

        if reading_rules:
            k, v = line.split("|")
            rules[k] = rules.get(k, []) + [v]
        else:
            updates.append(line.split(","))


def is_valid_update(update):
    for i, x in enumerate(update):
        if x in rules:
            required_descendants = rules[x]

            for required_descendant in required_descendants:
                if required_descendant in update[:i]:
                    return False

    return True


def get_middle_key(input):
    i, update = input
    midpoint = len(update) // 2

    return int(update[midpoint])


def solution_1():
    valid_updates = filter(is_valid_update, updates)

    print("Solution 1:", sum(map(get_middle_key, enumerate(valid_updates))))


def solution_2():
    valid_updates = []

    def comparator(a, b):
        if a in rules[b]:
            return -1
        elif b in rules[a]:
            return 1
        else:
            return 0

    for update in updates:
        if not is_valid_update(update):
            sorted_update = sorted(update, key=cmp_to_key(comparator))
            valid_updates.append(sorted_update)

    print("Solution 2:", sum(map(get_middle_key, enumerate(valid_updates))))


solution_1()
solution_2()
