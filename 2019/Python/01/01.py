import numpy as np

data = [int(x) for x in open('input', 'r').read().strip().split('\n')]

masses = np.array(data)
def fuel_need(mass):
    return np.maximum(mass // 3 - 2, 0)

fuel = fuel_need(masses)
print("Part 1: ", np.sum(fuel))

dfuel = fuel.copy()
while True:
    dfuel = fuel_need(dfuel)
    if np.all(dfuel <= 0):
        break
    fuel += dfuel
print("Part 2: ", np.sum(fuel))