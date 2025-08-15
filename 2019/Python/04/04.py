import re

lbound, ubound = (int(x) for x in open('input', 'r').read().strip().split('-'))

double = re.compile(r'(.)\1')

def meets_criteria(num):
    num_str = str(num)
    for i in range(len(num_str)-1):
        if int(num_str[i+1])<int(num_str[i]):
            return False

    if double.search(num_str):
        return True
    return False

total = 0
for i in range(int(lbound), int(ubound)+1):
    if meets_criteria(i):
        total += 1
print("Part 1:", total)