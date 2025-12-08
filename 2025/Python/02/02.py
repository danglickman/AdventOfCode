data = open('input', 'r').read().strip().split(',')
ranges = [id_range.split('-') for id_range in data]
p1=0
p2  = 0
for beg, end in ranges:
    beg = int(beg)
    end = int(end)
    for i in range(beg, end+1):
        s = str(i)
        l = len(s)
        if s[:l//2] == s[l//2:]:
            p1 += i
        if s in (s+s)[1:-1]:
            p2 += i

print("Part 1:", p1)
print("Part 2:", p2)