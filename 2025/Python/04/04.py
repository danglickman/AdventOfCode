from itertools import product

data = open('input', 'r').read().strip().split('\n')

pad_row = (len(data)+2) * "."

padded = [pad_row] + ['.' + row + "." for row in data] + [pad_row]
padded = [list(row) for row in padded]

p1 = 0
done = False
while not done:
    done = True
    for i in range(1, len(padded)-1):
        for j in range(1, len(padded)-1):
            adj_count = 0
            if padded[i][j] == ".":
                continue
            for dx, dy in product((-1, 0, 1), repeat=2):
                if dx == 0 and dy == 0:
                    continue
                else:
                    if padded[i + dx][j + dy] == '@':
                        adj_count += 1
            if adj_count < 4:
                p1 += 1
                padded[i][j]= '.'
                done = False

# print('\n'.join(''"".join(row) for row in padded))
print("Part 1:", p1)