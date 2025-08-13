from hashlib import md5

number = 0
p1 = None
p2 = None
while True:
    hash = md5(("ckczppom"+ str(number)).encode('utf-8')).hexdigest()
    if hash.startswith("00000"):
        if p1 is None:
            p1 = number
        if hash.startswith("000000"):
            p2 = number
            break
    number += 1
print("Part 1:", p1)
print("Part 2:", p2)