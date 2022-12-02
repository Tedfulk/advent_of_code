with open("1d_2022/calories.txt", "r") as f:
    contents = f.read()
    groups = contents.split("\n\n")
    max_list = []
    for group in groups:
        item = group.splitlines()
        summ = sum([int(i) for i in item])
        max_list.append(summ)
        new_max = max(max_list)
    print(new_max)
    max_list.sort()
    print(sum(max_list[-3:]))
