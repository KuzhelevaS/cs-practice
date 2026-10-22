from pathlib import Path

path = Path(input()) # получаем имя файла

with open(path, encoding="utf-8") as log:
    for line in log:
        pass
