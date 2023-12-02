file = open("2023/Day 2/input.txt", 'r')

powers: list[int] = []

for line in file:
    line = line.strip()

    _, turns = line.split(':')
    sets: list[str] = turns.strip().split(';')

    buff: dict = { "red": 0, "green": 0, "blue": 0 }

    for set in sets:
        set = set.strip()

        cubes: list[str] = set.split(',')

        for cube in cubes:
            cube = cube.strip()

            number, color = cube.split()
            number: int = int(number)

            if number > buff[color]:
                buff[color] = number

    powers.append(buff['red'] * buff['green'] * buff['blue'])

print(sum(powers))

file.close()
