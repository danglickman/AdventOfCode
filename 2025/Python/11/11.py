import functools

data = open('input', 'r').read().strip().split('\n')

connections = {}

for line in data:
    device, outputs = line.split(':')
    connections[device] = outputs.split()

@functools.cache
def paths_out(start, target):
    if start==target:
        return 1
    elif start=="out":
        return 0
    else:
        return sum(paths_out(c, target) for c in connections[start])

print("Part 1", paths_out("you", "out"))

total = 0
total += paths_out("svr", "dac") * paths_out("dac", "fft") * paths_out("fft", "out")
total += paths_out("svr", "fft") * paths_out("fft", "dac") * paths_out("dac", "out")
print("Part 2", total)