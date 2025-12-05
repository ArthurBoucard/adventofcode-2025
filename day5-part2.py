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
        i = 0
        for line in f:
            if i < sepration_index - 1:
                ranges.append(line.strip())
            i += 1
        ranges_int = []
        for r in ranges:
            start, end = r.split("-")
            start = int(start)
            end = int(end)
            ranges_int.append((start, end))

        ranges_int.sort(key=lambda x: x[0])

        merged = []
        for start, end in ranges_int:
            if not merged or start > merged[-1][1] + 1:
                merged.append([start, end])
            else:
                merged[-1][1] = max(merged[-1][1], end)

        for start, end in merged:
            count = (end - start + 1)
            total += count
    print(total)


fresh_produce()
