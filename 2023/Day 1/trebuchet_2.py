import re


file = open("2023/Day 1/input.txt", 'r')

valid_digits: list[str] = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

numbers: list[int] = []

for line in file:
    line = line.strip()

    buff: list[int] = []

    for valid_digit in valid_digits:
        buff.append([m.start() for m in re.finditer(valid_digit, line)])

    for i in range(len(buff)):
        for j in buff[i]:
            line = line[:j] + str(i + 1) + line[j + 1:]

    numerics: list[str] = [character for character in line.strip() if character.isnumeric()]
    numbers.append(int(numerics[0] + numerics[-1]))

print(sum(numbers))

file.close()
