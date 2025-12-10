import itertools
import math
from operator import itemgetter

data = open('input', 'r').read().strip().split('\n')

boxes = [tuple(int(n) for n in row.split(',')) for row in data]

def distance(c):
    b1, b2 = c
    return math.dist(b1, b2)
    # return (b1[0] - b2[0])**2 + (b1[1] - b2[1])**2 + (b1[2] - b2[2])**2

# This is by far the most expensive step
combinations = sorted(itertools.combinations(boxes, 2), key=distance)

circuits = {box: [box, 1] for box in boxes}

def find(box):
    parent, size = circuits[box]
    if parent != box:
        circuits[box][0] = find(parent)
        return circuits[box][0]
    return parent

def union(box1, box2):
    x = find(box1)
    y = find(box2)

    if x == y:
        return

    if circuits[x][1] < circuits[y][1]:
        x, y  = y, x

    circuits[y][0] = x
    circuits[x][1] = circuits[y][1] + circuits[x][1]
    if circuits[x][1] == len(data):
        print("Part 2:", box1[0] * box2[0])
        exit(0)


for b1, b2 in combinations[:1000]:
    union(b1, b2)

finals = [(box, info[1])for box, info in circuits.items() if box == info[0]]

finals.sort(key=itemgetter(1))
print("Part 1:", math.prod([x[1] for x in finals[-3:]]))

for b1, b2 in combinations[1000:]:
    union(b1, b2)
