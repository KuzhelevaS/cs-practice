import sys
from stats import read_valid

lines = sys.stdin.read().splitlines()
records = read_valid(lines)
print(records)
'''
best = ""
for city in total:
    if best == "" or total[city] / count[city] > total[best] / count[best]:
        best = city
print(len(lines))
print(0)
print(total[best] / count[best])
'''
