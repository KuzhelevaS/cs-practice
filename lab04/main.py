import sys
from stats import average_by_city, read_valid, warmest_city

lines = sys.stdin.read().splitlines()
records = read_valid(lines)
averages = average_by_city(records)
best = warmest_city(records)
print(len(records))
print(sum(1 for line in lines if line.strip()) - len(records))
print(f'{averages[best]:.1f}')
