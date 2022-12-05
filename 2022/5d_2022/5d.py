with open("5d_2022/supply_stacks.txt", "r") as f:
    lines = f.readlines()
    moves = [x.strip().split() for x in lines if x.startswith("move")]
    # print(moves)
    rows = [line[1::4] for line in lines[:8]]
    stacks = {}
    for i in range(9):
        for row in rows[::-1]:
            if row[i] != ' ':
                stacks.setdefault(i+1, []).insert(0, row[i])
    # print(stacks)

def get_moves(moves: list[str]) -> list[int]:
    move_list = []
    for move in moves:
        # print([int(move[1]), int(move[3]), int(move[5])])
        move_list.append([int(move[1]), int(move[3]), int(move[5])])
    return move_list
# print(get_moves(moves))
# get_moves =  [[1, 2, 1], [3, 1, 3], [2, 2, 1], [1, 1, 2]]
# stacks = {1: ['N', 'Z'], 2:['D', 'C', 'M'], 3:['P']}


def mover(move, stacks: dict[int, list[str]]):
    count, frm, to = move
    from_stack = stacks[frm]
    to_stack = stacks[to]
    for _ in range(count):
        crate = from_stack.pop(0)
        to_stack.insert(0, crate)
    return stacks

# print(mover([1,2,1], stacks))
for move in get_moves(moves):
    stacks = mover(move, stacks)
# print(stacks.values())
tops = ''
for v in stacks.values():
    tops += v[0]
print(tops)



