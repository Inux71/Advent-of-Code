file = open("2023/Day 1/input.txt", 'r')

numbers: list[int] = []

for line in file:
    numerics: list[str] = [character for character in line.strip() if character.isnumeric()]
    numbers.append(int(numerics[0] + numerics[-1]))

print(sum(numbers))

file.close()
