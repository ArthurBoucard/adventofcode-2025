def batteries():
    total = 0
    with open("inputs/day3.txt", "r") as f:
        for line in f:
            line = line.strip()
            high = 0
            pos = 0
            temp = 0
            battery_index = 12
            while battery_index > 0:
                for i in range(pos, len(line) - battery_index + 1):
                    if int(line[i]) > high:
                        high = int(line[i])
                        pos = i + 1
                temp += high * (10 ** (battery_index - 1))
                high = 0
                battery_index -= 1
            total += temp

    print(total)

batteries()
