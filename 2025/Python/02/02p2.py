data = open('input', 'r').read().strip().split(',')
ranges = [id_range.split('-') for id_range in data]

def is_valid(n):
    s = str(n)
    l = len(s)

    for i in range(1, l//2+1):
        if l % i == 0:
            for j in range(i):
                first = s[j]
                if not all(char == first for char in s[j::i]):
                    break
            else:
                return False

    return True


p2  = 0
for beg, end in ranges:
    beg = int(beg)
    end = int(end)
    for i in range(beg, end+1):
        s = str(i)
        l = len(s)
        if not is_valid(i):
            p2 += i


print(p2)