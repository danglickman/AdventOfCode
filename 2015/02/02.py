from itertools import combinations

data = open('input', 'r').read().strip().split('\n')

dims = [list(int(dim) for dim in line.split('x')) for line in data]
total_area = 0
total_ribbon = 0
for gift in dims:
    side_areas = list(a*b for a, b in combinations(gift, 2))
    a, b, c = sorted(gift)
    total_ribbon += 2*(a+b) + a*b*c
    total_area += (2 * sum(side_areas)) + min(side_areas)

print(f"Part 1: {total_area}")
print(f"Part 2: {total_ribbon}")