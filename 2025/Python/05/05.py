fr, ids = open('input', 'r').read().strip().split('\n\n')

fr = [tuple(int(id) for id in entry.split('-')) for entry in fr.split('\n')]
ids = [int(id) for id in ids.split('\n')]

intervals = sorted(fr)
merged_intervals = []


p2 = 0
beg  = intervals[0][0]
end = intervals[0][1]

# using indexes maybe nicer?
for a, b in intervals[1:]:
    if b <= end: #included
        continue
    if a <= end:
        end =  max(end, b)
    else: # no overlap
        merged_intervals.append((beg, end))
        beg = a
        end = b
merged_intervals.append((beg, end))

p1 = 0
for id in ids:
    for r in merged_intervals:
        if r[0] <= id <= r[1]:
            break
    else:
        continue
    p1 += 1
print("Part 1:", p1)

for a, b in merged_intervals:
    p2 += b - a + 1
print("Part 2:", p2)
