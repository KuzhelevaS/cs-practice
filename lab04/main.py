import sys
from stats import average_by_city, read_valid

lines = sys.stdin.read().splitlines()
records, errs = read_valid(lines)
print(len(records))
print(errs)
'''
best = ""
for city in total:
    if best == "" or total[city] / count[city] > total[best] / count[best]:
        best = city
print(len(lines))
print(0)
print(total[best] / count[best])
'''
