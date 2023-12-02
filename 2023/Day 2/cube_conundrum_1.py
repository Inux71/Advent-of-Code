file = open("2023/Day 2/input.txt", 'r')

possible_game: dict = { "red": 12, "green": 13, "blue": 14 }
id_sum: int = 0

for line in file:
    line = line.strip()

    game, turns = line.split(':')
    id: int = game.strip().split(' ')[1]
    sets: list[str] = turns.strip().split(';')

    possible: bool = True

    for set in sets:
        set = set.strip()

        buff: dict = { "red": 0, "green": 0, "blue": 0 }

        cubes: list[str] = set.split(',')

        for cube in cubes:
            cube = cube.strip()

            number, color = cube.split()
            number = int(number)

            buff[color] += number

            if buff["red"] > possible_game["red"] or buff["green"] > possible_game["green"] or buff["blue"] > possible_game["blue"]:
                possible = False
                break
        
        if possible is False:
            break
    
    if possible:
        id_sum += int(id)

print(id_sum)

file.close()
