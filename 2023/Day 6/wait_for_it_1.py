import re
import math


file = open("2023/Day 6/input.txt", 'r')

data: list[list[int]] = [list(map(int, re.findall(r"\d+", line.strip()))) for line in file]
ways: list[int] = []

for i in range(len(data[0])):
    w: int = 0

    for j in range(1, data[0][i] + 1):
        if j * (data[0][i] - j) > data[1][i]:
            w += 1

    ways.append(w)

print(math.prod(ways))

file.close()
