data = open('input', 'r').read().strip().split(',')
ranges = [id_range.split('-') for id_range in data]
p1=0
for beg, end in ranges:
    beg = int(beg)
    end = int(end)
    for i in range(beg, end+1):
        s = str(i)
        l = len(s)
        if s[:l//2] == s[l//2:]:
            p1 += i

print(p1)