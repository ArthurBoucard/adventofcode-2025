def batteries():
    total = 0
    with open("inputs/day3.txt", "r") as f:
        for line in f:
            line = line.strip()
            high_dec = 0
            pos_dec = 0
            high_unit = 0
            for i in range(0, len(line) - 1):
                if int(line[i]) > high_dec:
                    high_dec = int(line[i])
                    pos_dec = i
            for j in range(pos_dec + 1, len(line)):
                if int(line[j]) > high_unit:
                    high_unit = int(line[j])
            total += (high_dec * 10) + high_unit

    print(total)

batteries()
