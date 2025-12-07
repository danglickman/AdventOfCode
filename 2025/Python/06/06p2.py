import operator
from functools import reduce

data = open('input', 'r').read().strip("\n").split('\n')

nums = []
ops = []
col = []
num = 0
for i in range(len(data[0])-1, -1, -1):
    for j in range(len(data)-1):
        if data[j][i].isdigit():
            num *= 10
            num += int(data[j][i])
        elif data[j][i]==' ':
            pass
    if num != 0:
        col.append(num)
        num = 0
    if data[len(data)-1][i] != ' ':
        nums.append(col)
        col = []
        ops.append(data[len(data)-1][i])

total = 0
for op, num in zip(ops, nums):
    if op == "+":
        op = operator.add
    else:
        op = operator.mul

    total += reduce(op, num)
print(total)

