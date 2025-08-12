data = open('input', 'r').read().strip()

floor = 0
part2 = -1
for i, x in enumerate(data):
    if x == '(':
        floor += 1
    elif x == ')':
        floor -= 1
    if part2 == -1 and floor == -1:
        part2 = i + 1

print(f"Part 1: {floor}")
print(f"Part 2: {part2}")