file = open("2023/Day 15/input.txt", 'r')

data: list[str] = file.readline().strip().split(',')

sum: int = 0

for word in data:
    current_value: int = 0

    for character in word:
        current_value += ord(character)
        current_value *= 17
        current_value %= 256

    sum += current_value

print(sum)

file.close()
