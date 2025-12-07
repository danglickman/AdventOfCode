data = open('input', 'r').read().strip().split('\n')

pos = 50
p1 = 0
p2 = 0
for op in data:
    if op[0] == 'L':
        direction = -1
    else:
        direction = 1
    rot = int(op[1:])

    # transformation to avoid dealing with negative integer divmod
    pos = (direction * pos) % 100

    pos += rot
    times, rem = divmod(pos, 100)
    pos = rem

    p2 += times

    pos = (direction * pos) % 100

    if pos == 0:
        p1 += 1

print("Part 1:", p1)
print("Part 2:", p2)