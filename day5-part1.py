def fresh_produce():
    total = 0
    with open("inputs/day5.txt", "r") as f:
        sepration_index = 0
        for line in f:
            sepration_index += 1
            if line == "\n":
                break
        f.seek(0)
        ranges = []
        products = []
        i = 0
        for line in f:
            if i < sepration_index - 1:
                ranges.append(line.strip())
            elif i > sepration_index - 1:
                products.append(line.strip())
            i += 1
        for product in products:
            found = False
            product = int(product)
            for r in ranges:
                start, end = r.split("-")
                start = int(start)
                end = int(end)
                if start <= product <= end:
                    total += 1
                    break
    print(total)


fresh_produce()
