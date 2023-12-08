file = open("2023/Day 8/input.txt", 'r')

moves: str = file.readline().strip()
nodes: dict = {}

current_move: str = "AAA"
current_move_index: int = 0
steps: int = 0

file.readline()

for line in file:
    key, values = line.strip().split('=')
    key = key.strip()
    values = [v.strip() for v in values.strip()[1:-1].split(',')]

    nodes[key] = values

while current_move != "ZZZ":
    if moves[current_move_index] == 'L':
        current_move = nodes[current_move][0]
    else:
        current_move = nodes[current_move][1]

    current_move_index += 1
    current_move_index %= len(moves)
    
    steps += 1

print(steps)

file.close()
