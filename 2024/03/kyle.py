import re

input = ''

filename = './input.txt'

with open(filename, 'r') as file:
    for line in file:
        input += line.strip()

problem_1_regexp = re.compile(r'(mul\(\d+,\d+\))')
problem_2_regexp = re.compile(r'(mul\(\d+,\d+\)|do\(\)|don\'t\(\))')

# change this to solve different problems 
regexp = problem_1_regexp

matches = regexp.findall(input)

sum = 0

enabled = True

for match in matches:
    if match == 'do()':
        enabled = True
        continue

    if match == 'don\'t()':
        enabled = False
        continue

    if enabled:
        nums = match[4:-1].split(',')
        sum += int(nums[0]) * int(nums[1])

print(sum)
