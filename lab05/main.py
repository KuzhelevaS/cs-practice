from pathlib import Path
from logstats import count_levels, top_errors, format_report

path = Path(input()) # получаем имя файла

with open(path, encoding="utf-8") as log:
    levels = count_levels(log)

with open(path, encoding="utf-8") as log:
    errors = top_errors(log, 3)

print(format_report(levels, errors))