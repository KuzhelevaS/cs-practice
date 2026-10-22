from functools import reduce
from pathlib import Path
from logstats import count_levels, top_errors, format_report, BROKEN_LEVEL

path = Path(input()) # получаем имя файла

with open(path, encoding="utf-8") as log:
    levels = count_levels(log)

with open(path, encoding="utf-8") as log:
    errors = top_errors(log, 3)

line_count = reduce(lambda x, y: x + y, levels.values(), 0)
print(line_count)
print(levels.get("ERROR"))
print(levels.get(BROKEN_LEVEL, 0))

with open("report.txt", "w", encoding="utf-8") as f:
    f.write(format_report(levels, errors))