def forklift():
    total = 0
    with open("inputs/day4.txt", "r") as f:
        rolls = []
        for line in f:
            rolls.append(line.strip())
        index = 0
        for line in rolls:
            for i in range(0, len(line)):
                if line[i] == "@":
                    total_next = 0
                    # left
                    if i != 0 and line[i - 1] == "@":
                        total_next += 1
                    #  right
                    if i != len(line) - 1 and line[i + 1] == "@" :
                        total_next += 1
                    if index < len(rolls) - 1:
                        # bottom left
                        if i != 0 and rolls[index + 1][i - 1] == "@":
                            total_next += 1
                        # bottom
                        if rolls[index + 1][i] == "@":
                            total_next += 1
                        # bottom right
                        if i != len(line) - 1 and rolls[index + 1][i + 1] == "@":
                            total_next += 1
                    if index != 0:
                        # top left
                        if i != 0 and rolls[index - 1][i - 1] == "@":
                            total_next += 1
                        # top
                        if rolls[index - 1][i] == "@":
                            total_next += 1
                        # top right
                        if i != len(line) - 1 and rolls[index - 1][i + 1] == "@":
                            total_next += 1
                    if total_next < 4:
                        total += 1
            index += 1
    print(total)

forklift()
