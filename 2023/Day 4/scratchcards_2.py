file = open("2023/Day 4/input.txt", 'r')

cards: list[str] = [line[line.index(':') + 1:].strip() for line in file]
indexes: list[int] = []

def find_indexes(current_index: int) -> None:
    winning_numbers, numbers = cards[current_index].split('|')
    winning_numbers = [n for n in winning_numbers.strip().split(' ') if n.isnumeric()]
    numbers = [n for n in numbers.strip().split(' ') if n.isnumeric()]

    matched_numbers: int = 0

    for winning_number in winning_numbers:
        if winning_number in numbers:
            matched_numbers += 1

    for i in range(matched_numbers):
        indexes.append(current_index + i + 2)

        find_indexes(current_index + i + 1)


for i in range(len(cards)):
    indexes.append(i + 1)

    find_indexes(i)

counts: dict = {}

for index in indexes:
    if index in counts:
        counts[index] += 1
    else:
        counts[index] = 1

print(sum(counts.values()))

file.close()
