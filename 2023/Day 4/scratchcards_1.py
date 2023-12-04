file = open("2023/Day 4/input.txt", 'r')

total_points: int = 0

for line in file:
    line = line[line.index(':') + 1:].strip()

    winning_numbers, numbers = line.split('|')
    winning_numbers = [n for n in winning_numbers.strip().split(' ') if n.isnumeric()]
    numbers = [n for n in numbers.strip().split(' ') if n.isnumeric()]

    matched_numbers: int = 0

    for winning_number in winning_numbers:
        if winning_number in numbers:
            matched_numbers += 1

    if matched_numbers > 0:
        total_points += pow(2, matched_numbers - 1)

print(total_points)

file.close()
