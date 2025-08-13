import re

data = open('input', 'r').read().strip().split('\n')

vowels = re.compile(r'[aeiou].*[aeiou].*[aeiou]')
double = re.compile(r'(.)\1')
naughty = re.compile(r'(ab|cd|pq|xy)')

nice_count = 0
for string in data:
    if vowels.search(string) and double.search(string) and not naughty.search(string):
        nice_count += 1
print("Part 1:", nice_count)


sep_pair = re.compile(r'(..).*\1')
rep = re.compile(r'(.).\1')

nice2 = 0
for string in data:
    if sep_pair.search(string) and rep.search(string):
        nice2 += 1
print("Part 2:", nice2)