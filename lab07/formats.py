import csv
import io
import json

def csv_to_records(text: str) -> list[dict]:
    if not text:
        return []

    reader = csv.DictReader(io.StringIO(text))
    if not reader.fieldnames:
        return []

    # обрезаем пробелы в заголовках
    fieldnames = [f.strip() for f in reader.fieldnames]
    records = []
    for row in reader:
        values = [row.get(f) for f in reader.fieldnames]
        if all(v is None or v == "" for v in values):
            continue

        record = {}
        for key, value in zip(reader.fieldnames, fieldnames):
            val = row.get(key)
            record[value] = "" if val is None else str(val).strip()
        records.append(record)
    return records

def get_value(value: str):
    low = value.lower()
    if low in ("true", "yes"):
        return True
    if low in ("false", "no"):
        return False

    try:
        return int(value)
    except ValueError:
        pass

    try:
        return float(value)
    except ValueError:
        return value


def parse_settings(lines: list[str]) -> dict:
    result = dict()
    current_list_key = None

    for raw in lines:
        line = raw.split("#", 1)[0].strip()
        if not line:
            continue

        if line[:2] == "- ":
            if current_list is not None:
                current_list.append(get_value(line[2:].strip()))
            continue

        if ":" in line:
            key, _, value = line.partition(":")
            key = key.strip()
            value = value.strip()

            if value == "":
                current_list = []
                result[key] = current_list
            else:
                result[key] = get_value(value)
                current_list = None

    return result

def merge_by_key(rows: list[dict], extra: dict, key: str = id) -> list[dict]:
    result = []

    for row in rows:
        k = row.get(key)
        addition = extra.get(k, {})

        temp = dict(addition)
        temp.update(row)
        result.append(temp)

    return result

def records_to_json(records: list[dict]) -> str:
    return json.dumps(records, ensure_ascii=False, indent=2, sort_keys=True)

def test():
    assert(csv_to_records("id,город\n1,Азов\n2,Шахты") == [{"id": "1", "город": "Азов"}, {"id": "2", "город": "Шахты"}])
    assert (csv_to_records("город, цена \n Азов , 100") == [{"цена": "100", "город": "Азов"}])
    assert(csv_to_records("") == [])

    settings1 = ["# отчёт", "title: Отчёт за март", "decimals: 1", "active: true", "columns:", "  - город", "  - цена"]
    assert(parse_settings(settings1) == {"title": "Отчёт за март", "decimals": 1, "active": True, "columns": ["город", "цена"]})
    assert parse_settings(["rate: 3,5 # с запятой"]) == {"rate": "3,5"}
    assert parse_settings([]) == dict()

    d1_1 = [{"id": "1", "город": "Азов"}]
    d2_1 = {"1": {"регион": "Ростовская"}}
    assert merge_by_key(d1_1, d2_1, "id") == [{"регион": "Ростовская", "id": "1", "город": "Азов"}]

    assert records_to_json([]) == "[]"
    assert records_to_json([{"б": 2, "а": 1}]) == """[
  {
    "а": 1,
    "б": 2
  }
]"""

if __name__ == "__main__":
    test()