from operator import indexOf

data = open('input', 'r').read().strip().split('\n')

banks = [[int(digit) for digit in bank] for bank in data]


def max_n(bank, n):
    l = len(bank)
    first = max(bank[:l-(n-1)])
    if n == 1:
        return first
    idx = indexOf(bank, first)
    rest = max_n(bank[idx+1:], n-1)
    return first * (10**(n-1)) + rest


p1 = 0
p2 = 0
for bank in banks:
    p1 += max_n(bank, 2)
    p2 += max_n(bank, 12)


print("part 1:", p1)
print("part 2:", p2)
