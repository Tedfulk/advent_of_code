with open("7d_2022/sample.txt", "r") as f:
    lines = f.read().replace("\n", "")
    # print(lines)


def first_start_of_packet_marker(data: str, marker_index: int):
    for i in range(marker_index, len(data)):
        sequence = data[i - marker_index : i]
        found = False
        for j in range(marker_index):
            for k in range(j + 1, marker_index):
                if sequence[j] == sequence[k]:
                    found = True

        if not found:
            return i


print(first_start_of_packet_marker(lines, 4))
print(first_start_of_packet_marker(lines, 14))
