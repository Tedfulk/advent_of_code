with open("3d_2022/rucksack.txt", "r") as f:
    data = [x for x in f.read().splitlines()]
    # print(data)
    for item in data:
        # print(int(len(item) / 2))
        part_1 = {item[: int(len(item) / 2)]}
        part_2 = {item[int(len(item) / 2) :]}
        # print(part_1, part_2)
        for char in part_1:
            group_1 = set(list(char))
        for char in part_2:
            group_2 = set(list(char))
        # print(group_1, group_2)
        diff = group_1.intersection(group_2)
        # print(diff)
        for char in diff:
            # print(char)
            if char.islower():
                # print(char)
                print(ord(char) - 96)
            if char.isupper():
                print(ord(char) - 38)

with open("3d_2022/part_1_output.txt", "r") as f:
    data = [int(x) for x in f.read().splitlines()]
    print(sum(data))

with open("3d_2022/rucksack.txt", "r") as f:
    data = [x for x in f.read().splitlines()]
    # print(data)
    groups = [data[i : i + 3] for i in range(0, len(data), 3)]
    set_groups = [map(set, group) for group in groups]
    groups = [set.intersection(*set_group).pop() for set_group in set_groups]
    # print(groups)
    for char in groups:
        # print(char)
        if char.islower():
            # print(char)
            print(ord(char) - 96)
        if char.isupper():
            print(ord(char) - 38)

with open("3d_2022/part_2_output.txt", "r") as f:
    data = [int(x) for x in f.read().splitlines()]
    print(sum(data))
