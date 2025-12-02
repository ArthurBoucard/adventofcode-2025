import math

def secret_entrance():
    with open("inputs/day1.txt", "r") as f:
        start = 50
        secret = 0
        for line in f:
            direction = line[0]
            temp_start = start
            if direction == "R":
                incr = int(line[1:])
                start = (start + incr) % 100
                if incr >= 100:
                    secret += math.floor(incr / 100)
                    if start == 0:
                        secret -= 1
                elif (temp_start + incr) > 99 and start != 0:
                    secret += 1
            elif direction == "L":
                incr = int(line[1:])
                start = (start - incr) % 100
                if incr >= 100:
                    secret += math.floor(incr / 100)
                    if start == 0:
                        secret -= 1
                elif (temp_start - incr) < 0 and start != 0:
                    secret += 1
            if start == 0:
                secret += 1
    print(secret)

secret_entrance()
