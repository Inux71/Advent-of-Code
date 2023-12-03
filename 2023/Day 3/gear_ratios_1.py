file = open("2023/Day 3/input.txt", 'r')

data: list[str] = [line.strip() for line in file]
sum: int = 0

i: int = 0

while i < len(data):
    j: int = 0

    while j < len(data[i]):
        if data[i][j].isnumeric():
            str_number: str = ""

            while j < len(data[i]) and data[i][j].isnumeric():
                str_number += data[i][j]
                j += 1

            l = len(str_number)

            # top-right
            if i > 0 and j < len(data[i]) and data[i - 1][j].isnumeric() is False and data[i - 1][j] != '.':
                sum += int(str_number)
                continue

            # right
            if j < len(data[i]) and data[i][j].isnumeric() is False and data[i][j] != '.':
                sum += int(str_number)
                continue

            # bottom-right
            if i + 1 < len(data) and j < len(data[i]) and data[i + 1][j].isnumeric() is False and data[i + 1][j] != '.':
                sum += int(str_number)
                continue

            # top-left
            if i > 0 and j - l > 0 and data[i - 1][j - l - 1].isnumeric() is False and data[i - 1][j - l - 1] != '.':
                sum += int(str_number)
                continue

            # left
            if j - l > 0 and data[i][j - l - 1].isnumeric() is False and data[i][j - l - 1] != '.':
                sum += int(str_number)
                continue

            # bottom-left
            if i + 1 < len(data) and j - l > 0 and data[i + 1][j - l - 1].isnumeric() is False and data[i + 1][j - l - 1] != '.':
                sum += int(str_number)
                continue

            # bottom
            if i + 1 < len(data):
                buff = data[i + 1][j - l:j]

                for b in buff:
                    if b.isnumeric() is False and b != '.':
                        sum += int(str_number)
                        break

            # top
            if i > 0:
                buff = data[i - 1][j - l:j]

                for b in buff:
                    if b.isnumeric() is False and b != '.':
                        sum += int(str_number)
                        break

        j += 1

    i += 1

print(sum)

file.close()
    