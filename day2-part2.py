def gift_shop():
    total = 0
    with open("inputs/day2.txt", "r") as f:
        line = f.read().strip()
        ranges = line.split(",")
        print(ranges)
        for r in ranges:
            a, b = r.split("-")
            start = int(a)
            end = int(b)
            while start <= end:
                id = str(start)
                cut_len = 1
                while cut_len <= len(id) // 2:
                    if len(id) % cut_len != 0 or len(id) // cut_len < 2:
                        cut_len += 1
                        continue
                    test = id[:cut_len]
                    same_same = True
                    for i in range(0, (len(id) // cut_len)):
                        if test != id[i * cut_len:(i * cut_len) + cut_len]:
                            same_same = False
                            break
                    if same_same == True:
                        total += start
                        break
                    cut_len += 1
                start += 1
    print(total)


gift_shop()
