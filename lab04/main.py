import sys

from stats import read_valid

lines = sys.stdin.read().splitlines()
total = {}
count = {}
records, errors = read_valid(lines)
for record in records:
    total[record["city"]] = total.get(record["city"], 0) + float(record["temp"])
    count[record["city"]] = count.get(record["city"], 0) + 1
best = ""
for city in total:
    if best == "" or total[city] / count[city] > total[best] / count[best]:
        best = city
print(len(records))
print(errors)
print(total[best] / count[best])
