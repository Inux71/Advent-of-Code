file = open("2023/Day 9/input.txt", 'r')

def all_zeros(n: list[int]) -> bool:
    for i in range(len(n)):
        if n[i] != 0:
            return False
        
    return True


sum: int = 0

for line in file:
    numbers: list[int] = [int(n) for n in line.strip().split(' ')]
    history: list[list[int]] = [numbers, [numbers[i] - numbers[i - 1] for i in range(1, len(numbers))]]

    while not all_zeros(history[-1]):
        history.append([history[-1][i] - history[-1][i - 1] for i in range(1, len(history[-1]))])

    history.pop()

    for i in range(len(history) - 1, 0, -1):
        history[i - 1].append(history[i - 1][-1] + history[i][-1])

    sum += history[0][-1]

print(sum)

file.close()
