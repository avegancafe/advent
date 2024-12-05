from typing import List, Dict

input = []

with open("./input.txt") as file:
    input.extend([list(line.strip().lower()) for line in file])


def solution_1():
    def score(i: int, j: int, matrix: List[List[str]]):
        fin = 0

        if matrix[i][j] == "x":
            try:
                if matrix[i][j + 1] == "m" and matrix[i][j + 2] == "a" and matrix[i][j + 3] == "s":
                    fin += 1
            except IndexError:
                pass

            try:
                if matrix[i + 1][j] == "m" and matrix[i + 2][j] == "a" and matrix[i + 3][j] == "s":
                    fin += 1
            except IndexError:
                pass

            try:
                if matrix[i + 1][j + 1] == "m" and matrix[i + 2][j + 2] == "a" and matrix[i + 3][j + 3] == "s":
                    fin += 1
            except IndexError:
                pass

            try:
                if (
                    j - 3 >= 0
                    and matrix[i + 1][j - 1] == "m"
                    and matrix[i + 2][j - 2] == "a"
                    and matrix[i + 3][j - 3] == "s"
                ):
                    fin += 1
            except IndexError:
                pass

            try:
                if j - 3 >= 0 and matrix[i][j - 1] == "m" and matrix[i][j - 2] == "a" and matrix[i][j - 3] == "s":
                    fin += 1
            except IndexError:
                pass

            try:
                if i - 3 >= 0 and matrix[i - 1][j] == "m" and matrix[i - 2][j] == "a" and matrix[i - 3][j] == "s":
                    fin += 1
            except IndexError:
                pass

            try:
                if (
                    i - 3 >= 0
                    and j - 3 >= 0
                    and matrix[i - 1][j - 1] == "m"
                    and matrix[i - 2][j - 2] == "a"
                    and matrix[i - 3][j - 3] == "s"
                ):
                    fin += 1
            except IndexError:
                pass

            try:
                if (
                    i - 3 >= 0
                    and matrix[i - 1][j + 1] == "m"
                    and matrix[i - 2][j + 2] == "a"
                    and matrix[i - 3][j + 3] == "s"
                ):
                    fin += 1
            except IndexError:
                pass

        return fin

    count = 0

    for i, x in enumerate(input):
        for j, y in enumerate(x):
            cur_score = score(i, j, input)

            if cur_score > 0:
                pass
                # print(f"Found MAS at ({i},{j}) with score {cur_score}")

            count += cur_score

    print(f"Solution 1: {count}")


def solution_2():
    def score(i, j, input):
        diag_1_seq = [(i - 1, j - 1), (i, j), (i + 1, j + 1)]
        diag_2_seq = [(i - 1, j + 1), (i, j), (i + 1, j - 1)]

        def within_bounds(x, y):
            return 0 <= x < len(input) and 0 <= y < len(input[0])

        diag_1_letters = "".join(input[x][y] if within_bounds(x, y) else "" for x, y in diag_1_seq)
        diag_2_letters = "".join(input[x][y] if within_bounds(x, y) else "" for x, y in diag_2_seq)

        count = 0

        for diag_1_test in ["mas", "sam"]:
            for diag_2_test in ["mas", "sam"]:
                if diag_1_test in diag_1_letters and diag_2_test in diag_2_letters:
                    count += 1
        return count

    count = 0

    for i, x in enumerate(input):
        for j, y in enumerate(x):
            cur_score = score(i, j, input)

            count += cur_score

    print(f"Solution 2: {count}")


solution_1()
solution_2()
