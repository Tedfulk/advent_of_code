with open("2d_2022/rps.txt", "r") as f:
    data = [x.split(" ") for x in f.read().splitlines()]
    # print(data)
    # [['A', 'Y'], ['B', 'X'], ['C', 'Z']]
    # A and X = Rock = 1
    # B and Y = Paper = 2
    # C and Z = Scissors = 3
    # win = 6
    # draw = 3
    # lose = 0
    score = 0
    for item_1, item_2 in data:
        if item_1 == "A":
            if item_2 == "Y":
                score += 8
            elif item_2 == "X":
                score += 4
            else:
                score += 3
        elif item_1 == "B":
            if item_2 == "Y":
                score += 5
            elif item_2 == "X":
                score += 1
            else:
                score += 9
        else:
            if item_2 == "Y":
                score += 2
            elif item_2 == "X":
                score += 7
            else:
                score += 6
    print(score)

    # B X = lose = 0
    # A Y = draw = 3
    # C Z = win = 6
    total = 0
    for item_1, item_2 in data:
        if item_1 == "A":
            if item_2 == "Y":
                total += 4
            elif item_2 == "X":
                total += 3
            else:
                total += 8
        elif item_1 == "B":
            if item_2 == "Y":
                total += 5
            elif item_2 == "X":
                total += 1
            else:
                total += 9
        else:
            if item_2 == "Y":
                total += 6
            elif item_2 == "X":
                total += 2
            else:
                total += 7
    print(total)
