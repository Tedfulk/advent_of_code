with open("4d_2022/cleanup.txt", "r") as f:
    data = [x.split(",") for x in f.read().splitlines()]
    # print(data)
    # [[[2, 4], [6, 8]], [[2, 3], [4, 5]], [[5, 7], [7, 9]], [[2, 8], [3, 7]], [[6, 6], [4, 6]], [[2, 6], [4, 8]]]
    pairs = [[[int(x) for x in elf.split("-")] for elf in pair] for pair in data]
    # print(pairs)
    total = 0
    for pair in pairs:
        # print(pair)
        if (pair[0][0] <= pair[1][0] and pair[0][1] >= pair[1][1]) or (
            pair[1][0] <= pair[0][0] and pair[1][1] >= pair[0][1]
        ):
            total += 1
    # print(total)

    part_2_total = 0
    for pair in pairs:
        print(pair)
        if (pair[0][0] <= pair[1][0] and pair[0][1] >= pair[1][0]) or (
            pair[1][0] <= pair[0][0] and pair[1][1] >= pair[0][0]
        ):
            part_2_total += 1
    print(part_2_total)
