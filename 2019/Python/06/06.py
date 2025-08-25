from collections import deque, defaultdict
from functools import cache

data = open("input", 'r').read().strip().splitlines()
orbit_rel = [x.split(')') for x in data]
centers = {sat:main for main, sat in orbit_rel}
satellites = defaultdict(list)
for main, sat in orbit_rel:
    satellites[main].append(sat)

@cache
def num_orbits(obj):
    if obj == "COM":
        return 0
    else:
        return 1 + num_orbits(centers[obj])

print("Part 1:", sum(num_orbits(obj) for obj in centers))


# Due to its structure one can actually symmetric difference the two paths to root
# but BFS occurred to me first and was easy (and fast) enough.
start = centers["YOU"]
frontier = deque()
frontier.append((start, 0))
visited = set()
while frontier:
    obj, depth = frontier.pop()
    if obj in visited:
        continue
    visited.add(obj)
    if obj == "SAN":
        print("Part 2:", depth-1)
        break
    depth = depth + 1
    for sat in satellites[obj]:
        frontier.append((sat, depth))
    if not obj == "COM":
        frontier.append((centers[obj], depth))