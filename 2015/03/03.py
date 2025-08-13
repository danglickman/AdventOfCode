from dataclasses import dataclass

data = open('input', 'r').read().strip()

@dataclass
class SantaLike:
    visited:set
    x:int=0
    y:int=0

p1santa = SantaLike({(0, 0)})
santas = list(SantaLike({(0, 0)}) for _ in range(2))
curr = 0
for char in data:
    santa = santas[curr]
    if char == '^':
        p1santa.y += 1
        santa.y += 1
    elif char == 'v':
        p1santa.y -= 1
        santa.y -= 1
    elif char == '>':
        p1santa.x += 1
        santa.x += 1
    elif char == '<':
        p1santa.x -= 1
        santa.x -= 1
    p1santa.visited.add((p1santa.x, p1santa.y))
    santa.visited.add((santa.x, santa.y))
    curr = (curr + 1)%2

print("Part 1:", len(p1santa.visited))

p2_all_visited = santas[0].visited.union(santas[1].visited)
print("Part 2:", len(p2_all_visited))
