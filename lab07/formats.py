import csv
import io

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

def test():
    assert(csv_to_records("id,город\n1,Азов\n2,Шахты") == [{"id": "1", "город": "Азов"}, {"id": "2", "город": "Шахты"}])
    assert (csv_to_records("город, цена \n Азов , 100") == [{"цена": "100", "город": "Азов"}])
    assert(csv_to_records("") == [])


if __name__ == "__main__":
    test()