import sys

from stats import parse_record

lines = sys.stdin.read().splitlines()
total = {}
count = {}
for line in lines:
    data = parse_record(line)
    total[data["city"]] = total.get(data["city"], 0) + float(data["temp"])
    count[data["city"]] = count.get(data["city"], 0) + 1
best = ""
for city in total:
    if best == "" or total[city] / count[city] > total[best] / count[best]:
        best = city
print(len(lines))
print(0)
print(total[best] / count[best])
