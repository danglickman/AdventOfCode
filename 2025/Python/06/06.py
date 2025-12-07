import numpy as np


data = open('input', 'r').read().strip().split('\n')

nums = [[int(n) for n in row.split()] for row in data[:-1]]
nums = np.array(nums)
print(nums)

ops = data[-1].split()
ops = [np.add if op == '+' else np.multiply for op in ops]
print(ops)

totals = np.zeros_like(nums[0])
for i, op in enumerate(ops):
    totals[i] = op.reduce(nums[:,i])

print(np.sum(totals))