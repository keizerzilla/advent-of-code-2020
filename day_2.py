import re

# Parte 1
valids = 0
with open("input_2.txt", "r") as infile:
    for line in infile.readlines():
        parts = line.strip().split(" ")
        mini, maxi = parts[0].split("-")
        mini = int(mini)
        maxi = int(maxi)
        char = parts[1].replace(":", "")
        string = parts[2]
        count = string.count(char)
        if count >= mini and count <= maxi:
            valids += 1

print("Valids: {}".format(valids))

# Parte 2
valids = 0
with open("input_2.txt", "r") as infile:
    for line in infile.readlines():
        parts = line.strip().split(" ")
        mini, maxi = parts[0].split("-")
        p1 = int(mini)
        p2 = int(maxi)
        char = parts[1].replace(":", "")
        string = parts[2]
        if ((string[p1-1] == char) + (string[p2-1] == char)) == 1:
            valids += 1

print("Valids: {}".format(valids))

