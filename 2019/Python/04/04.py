from collections import Counter

lbound, ubound = (int(x) for x in open('input', 'r').read().strip().split('-'))

p1total = 0
p2total = 0
## monotonicity means repeated digits are consecutive
for i in range(lbound, ubound + 1):
    x = str(i)
    if  x == ''.join(sorted(x)):
        c = Counter(x)
        if max(c.values()) >= 2:
            p1total += 1
            if 2 in Counter(x).values():
                p2total += 1

print("Part 1:", p1total)
print("Part 2:", p2total)