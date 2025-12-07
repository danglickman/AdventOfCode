from functools import cache

data = open('input', 'r').read().strip().split('\n')

start = data[0].index('S')
beams = {start}

splits = 0
for row in data[1:]:
    for i, char in enumerate(row):
        if char == '^':
            if i in beams:
                beams.remove(i)
                beams.add(i-1)
                beams.add(i+1)
                splits += 1

print(splits)

@cache
def paths (r, c):
    r += 1
    if r + 1 == len(data):
        return 1
    if data[r][c] == '^':
        return paths(r, c-1) + paths(r, c+1)
    else:
        return paths(r, c)

print(paths(0, start))