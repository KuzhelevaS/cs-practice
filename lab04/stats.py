def parse_record(line: str) -> dict:
    if line.count(";") != 2:
        raise ValueError("wrong format")
    
    city, temp, date = line.split(";")
    if city == "" or date == "":
        raise ValueError("empty field")

    result = dict()
    result["city"] = city
    result["temp"] = float(temp)
    result["date"] = date
    return result

def read_valid(lines: list[str]) -> list[dict]:
    result = []
    err = 0
    for line in lines:
        if len(line) == 0:
            continue
        try:
            result.append(parse_record(line))
        except ValueError:
            print(f"невозможно обработать строку: \"{line}\"")
            err += 1

    return result, err

def average_by_city(records: list[dict]) -> dict:
    total = {}
    count = {}
    for record in records:
        total[record["city"]] = total.get(record["city"], 0) + record["temp"]
        count[record["city"]] = count.get(record["city"], 0) + 1
    result = dict()
    for city in total:
        result[city] = total[city] / count[city]
    return result

def warmest_city(records: list[dict]) -> str:
    best = ""
    for city in records:
        if best == "" or records[city] > records[best]:
            best = city
        elif records[city] == records[best]:
            best = min(city, best)
    return best

def ks_catch_exception(method, arg):
    try:
        method(arg)
    except Exception as e:
        return e.__class__


if __name__ == "__main__":
    d1 = {"city": "Азов", "temp": 24.5, "date": "2026-07-01"}
    assert parse_record("Азов;24.5;2026-07-01") == d1
    d2 = {"city": "Таганрог", "temp": 30.0, "date": "2026-07-01"}
    assert parse_record("Таганрог;30;2026-07-01") == d2
    assert ks_catch_exception(parse_record, "Азов;24.5;2026-07-01;") is ValueError
    assert ks_catch_exception(parse_record, ";24.5;2026-07-01") is ValueError
    assert ks_catch_exception(parse_record, "Азов;двадцать четыре;2026-07-01") is ValueError
    assert ks_catch_exception(parse_record, "Азов;;2026-07-01") is ValueError
    assert ks_catch_exception(parse_record, "Азов;25;") is ValueError

    s1 = ["Азов;24.5;2026-07-01",
        "Таганрог;30;2026-07-01",
        "Азов;25.5;2026-07-02"]
    l1 = [ {"city": "Азов", "temp": 24.5, "date": "2026-07-01"},
           {"city": "Таганрог", "temp": 30.0, "date": "2026-07-01"},
           {"city": "Азов", "temp": 25.5, "date": "2026-07-02"}]
    r1 = read_valid(s1)
    assert r1[0] == l1
    assert r1[1] == 0

    s2 = ["Азов;24.5;2026-07-01", "",
          "Таганрог;30;2026-07-01",
          "Азов;25.5;2026-07-02"]
    l2 = [{"city": "Азов", "temp": 24.5, "date": "2026-07-01"},
          {"city": "Таганрог", "temp": 30.0, "date": "2026-07-01"},
          {"city": "Азов", "temp": 25.5, "date": "2026-07-02"}]
    r2 = read_valid(s2)
    assert r2[0] == l2
    assert r2[1] == 0

    s3 = ["Азов;24.5;2026-07-01", ";;",
          "Таганрог;30;2026-07-01",
          "Азов;н/д;2026-07-02"]
    l3 = [{"city": "Азов", "temp": 24.5, "date": "2026-07-01"},
          {"city": "Таганрог", "temp": 30.0, "date": "2026-07-01"}]
    r3 = read_valid(s3)
    assert r3[0] == l3
    assert r3[1] == 2

    r4 = {"Азов": 25.0, "Таганрог": 30.0}
    assert average_by_city(l1) == r4

    assert warmest_city(r4) == "Таганрог"

    r5 = {"Азов": 30.0, "Таганрог": 25.0}
    assert warmest_city(r5) == "Азов"

    r6 = {"Азов": 30.0, "Аксай": 30.0}
    assert warmest_city(r6) == "Азов"

    r6 = {"Аксай": 30.0, "Азов": 30.0}
    assert warmest_city(r6) == "Азов"
