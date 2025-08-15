data = [wire.split(',') for wire in open('input', 'r').read().strip().split('\n')]

directions = {
    'U': (0, 1),
    'D': (0, -1),
    'L': (-1, 0),
    'R': (1, 0)
}

steps_to = [{}, {}]
for i, wire in enumerate(data):
    steps = 0
    x, y = 0, 0

    for inst in wire:
        dir = inst[0]
        dist = int(inst[1:])
        for _ in range(dist):
            x += directions[dir][0]
            y += directions[dir][1]
            steps += 1
            steps_to[i][(x, y)] = steps

crossings = set(steps_to[0].keys()).intersection(set(steps_to[1].keys()))

print("Part 1:", min(abs(x)+abs(y) for x,y in crossings))
print("Part 2:", min(steps_to[0][pos] + steps_to[1][pos] for pos in crossings))