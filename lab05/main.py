from pathlib import Path
from logstats import count_levels

path = Path(input()) # получаем имя файла

with open(path, encoding="utf-8") as log:
    levels = count_levels(log)

print(levels)