from pathlib import Path
from logstats import parse_event

path = Path(input()) # получаем имя файла

with open(path, encoding="utf-8") as log:
    for line in log:
        print(parse_event(line))
