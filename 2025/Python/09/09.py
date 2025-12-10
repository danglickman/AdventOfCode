import itertools

data = open('input', 'r').read().strip().split('\n')

red = [tuple(map(int, row.split(','))) for row in data]

sizes = [((abs(p1[0]-p2[0]) +1) * (abs(p1[1]-p2[1]) +1) , (p1, p2)) for p1, p2 in itertools.combinations(red, 2)]
sizes.sort(reverse=True)
print("Part 1:", sizes[0][0])

lines = list(itertools.pairwise(itertools.chain(red, [red[0]])))
vlines = [(c1, min(r1, r2), max(r1, r2)) for (c1, r1), (c2, r2) in lines if c1==c2]
hlines = [(r1, min(c1, c2), max(c1, c2)) for (c1, r1), (c2, r2) in lines if r1==r2]

max_gr_size = 0
for size, (t1,t2) in sizes:
    c1, r1 = t1
    c2, r2 = t2
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

print("Part 2: ", max_gr_size)