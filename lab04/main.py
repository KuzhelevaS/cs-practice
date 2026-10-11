import sys

from stats import average_by_city, read_valid, warmest_city

lines = sys.stdin.read().splitlines()

records, errors = read_valid(lines)
averages = average_by_city(records)
best = warmest_city(averages)
print(len(records))
print(errors)
print(averages[best])
