# import itertools

data = open('input', 'r').read().strip().split('\n\n')

# ss = data[:-1]
rs = data[-1]

# shapes = []
# for entry in ss:
#     id, *rows = entry.split('\n')
#     id = int(id[:-1])
#     shape = [[1 if c=='#' else 0 for c in row] for row in rows]
#     shapes.append(shape)
# for s in shapes:
#     shape_size = sum(itertools.chain(*s))

regions = []
for r in rs.split('\n'):
    dims, boxes = r.split(':')
    dims = tuple(map(int, dims.split('x')))
    boxes = tuple(map(int, boxes.strip().split(' ')))
    regions.append((dims, boxes))

total = 0
for dims, boxes in regions:
    w, h = dims
    area = w * h
    n_boxes = sum(boxes)
    if (w//3) * (h//3) >= n_boxes:
        total += 1
        # print("Approved")
        continue
    if area <= n_boxes*7:
        # print("fail")
        continue
    print("unknown")
print(total)

