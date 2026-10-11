import sys

from stats import average_by_city, read_valid

lines = sys.stdin.read().splitlines()

records, errors = read_valid(lines)
averages = average_by_city(records)
best = ""
for city in averages:
    if best == "" or averages[city] > averages[best]:
        best = city
print(len(records))
print(errors)
print(averages[best])
