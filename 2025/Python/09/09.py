import itertools

data = open('input', 'r').read().strip().split('\n')

red = [tuple(map(int, row.split(','))) for row in data]

assert(len(red) == len(set(red)))

r_max = max(r for _, r in red)
c_max = max(c for c, r in red)


lines = list(itertools.pairwise(itertools.chain(red, [red[0]])))
vlines = [(c1, min(r1, r2), max(r1, r2)) for (c1, r1), (c2, r2) in lines if c1==c2]
hlines = [(r1, min(c1, c2), max(c1, c2)) for (c1, r1), (c2, r2) in lines if r1==r2]

max_size = 0
max_gr_size = 0
for t1,t2 in itertools.combinations(red, 2):
    c1, r1 = t1
    c2, r2 = t2
    dx = abs(t1[0] - t2[0])+1
    dy = abs(t1[1] - t2[1])+1
    size = dx*dy
    if size > max_size:
        max_size = size
    if size > max_gr_size:
        c_max = max(c1, c2)
        r_max = max(r1, r2)
        c_min = min(c1, c2)
        r_min = min(r1, r2)
        fail = False
        for c, r1, r2 in vlines:
            if c_min < c < c_max:
                if r1 < r_max <= r2 or r1 <= r_min < r2:
                    fail = True
                    break
        else:
            for r, c1, c2 in hlines:
                if r_min < r < r_max:
                    if c1 < c_max <= c2 or c1 <= c_min < c2:
                        fail = True
                        break
        if not fail:
            max_gr_size = size

print("Part 1: ", max_size)
print("Part 2: ", max_gr_size)



