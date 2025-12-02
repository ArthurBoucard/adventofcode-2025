def secret_entrance():
    with open("inputs/day1.txt", "r") as f:
        start = 50
        secret = 0
        for line in f:
            direction = line[0]
            if direction == "R":
                start = (start + int(line[1:])) % 100
            elif direction == "L":
                start = (start -int(line[1:])) % 100
            if start == 0:
                secret += 1
    print(secret)

secret_entrance()
