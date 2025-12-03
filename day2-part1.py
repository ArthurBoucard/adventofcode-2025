def gift_shop():
    total = 0
    with open("inputs/day2.txt", "r") as f:
        line = f.read().strip()
        ranges = line.split(",")
        print(ranges)
        for range in ranges:
            a, b = range.split("-")
            start = int(a)
            end = int(b)
            while start <= end:
                id = str(start)
                if len(id) % 2 != 0:
                    start += 1
                    continue
                mid_index = len(id) // 2
                id_start = id[:mid_index]
                id_end = id[mid_index:]
                if id_start == id_end:
                    total += start
                start += 1
    print(total)


gift_shop()
