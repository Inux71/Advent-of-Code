import re


file = open("2023/Day 6/input.txt", 'r')

data: list[str] = [int(line[line.find(':') + 1:].strip().replace(' ', '')) for line in file]
ways: int = 0

for i in range(1, data[0] + 1):
    if i * (data[0] - i) > data[1]:
            ways += 1

print(ways)

file.close()
