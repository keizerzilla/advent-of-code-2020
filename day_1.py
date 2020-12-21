from itertools import combinations

# Parte 01
with open("input_1.txt", "r") as infile:
    nums = [int(line.strip()) for line in infile.readlines()]
    for a, b in combinations(nums, 2):
        if a + b == 2020:
            print(a, b, a*b)
            break

# Parte 02
with open("input_1.txt", "r") as infile:
    nums = [int(line.strip()) for line in infile.readlines()]
    for a, b, c in combinations(nums, 3):
        if a + b + c == 2020:
            print(a, b, c, a*b*c)
            break

