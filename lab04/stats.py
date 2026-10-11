def parse_record(line: str) -> dict:
    if line.count(";") != 2:
        raise ValueError("wrong format")
    
    city, temp, date = map(str.strip, line.split(";"))
    if city == "" or date == "":
        raise ValueError("empty field")

    result = dict()
    result["city"] = city
    result["temperature"] = float(temp.replace(",", "."))
    result["date"] = date
    return result

def read_valid(lines: list[str]) -> list[dict]:
    result = []
    for line in lines:
        if len(line) == 0:
            continue
        try:
            result.append(parse_record(line))
        except ValueError:
            pass

    return result

def average_by_city(records: list[dict]) -> dict:
    total = {}
    count = {}
    for record in records:
        total[record["city"]] = total.get(record["city"], 0) + record["temperature"]
        count[record["city"]] = count.get(record["city"], 0) + 1
    result = dict()
    for city in total:
        result[city] = total[city] / count[city]
    return result

def warmest_city(records: list[dict]) -> str:
    averages = average_by_city(records)
    best = ""
    for city in averages:
        if best == "" or averages[city] > averages[best]:
            best = city
        elif averages[city] == averages[best]:
            best = min(city, best)
    return best

def ks_catch_exception(method, arg):
    try:
        method(arg)
    except Exception as e:
        return e.__class__


if __name__ == "__main__":
    d1 = {"city": "Азов", "temperature": 24.5, "date": "2026-07-01"}
    assert parse_record("Азов;24.5;2026-07-01") == d1
    d2 = {"city": "Таганрог", "temperature": 30.0, "date": "2026-07-01"}
    assert parse_record("Таганрог;30;2026-07-01") == d2
    assert parse_record(" Таганрог ;30,0;2026-07-01") == d2
    assert ks_catch_exception(parse_record, "Азов;24.5;2026-07-01;") is ValueError
    assert ks_catch_exception(parse_record, ";24.5;2026-07-01") is ValueError
    assert ks_catch_exception(parse_record, "Азов;двадцать четыре;2026-07-01") is ValueError
    assert ks_catch_exception(parse_record, "Азов;;2026-07-01") is ValueError
    assert ks_catch_exception(parse_record, "Азов;25;") is ValueError

    s1 = ["Азов;24.5;2026-07-01",
        "Таганрог;30;2026-07-01",
        "Азов;25.5;2026-07-02"]
    l1 = [ {"city": "Азов", "temperature": 24.5, "date": "2026-07-01"},
           {"city": "Таганрог", "temperature": 30.0, "date": "2026-07-01"},
           {"city": "Азов", "temperature": 25.5, "date": "2026-07-02"}]
    assert read_valid(s1) == l1

    s2 = ["Азов;24.5;2026-07-01", "",
          "Таганрог;30;2026-07-01",
          "Азов;25.5;2026-07-02"]
    l2 = [{"city": "Азов", "temperature": 24.5, "date": "2026-07-01"},
          {"city": "Таганрог", "temperature": 30.0, "date": "2026-07-01"},
          {"city": "Азов", "temperature": 25.5, "date": "2026-07-02"}]
    assert read_valid(s2) == l2

    s3 = ["Азов;24.5;2026-07-01", ";;",
          "Таганрог;30;2026-07-01",
          "Азов;н/д;2026-07-02"]
    l3 = [{"city": "Азов", "temperature": 24.5, "date": "2026-07-01"},
          {"city": "Таганрог", "temperature": 30.0, "date": "2026-07-01"}]
    assert read_valid(s3) == l3

    r4 = {"Азов": 25.0, "Таганрог": 30.0}
    assert average_by_city(l1) == r4

    assert warmest_city(l2) == "Таганрог"

    l5 = [{"city": "Азов", "temperature": 30.0, "date": "2026-07-01"},
          {"city": "Таганрог", "temperature": 25.0, "date": "2026-07-01"}]
    assert warmest_city(l5) == "Азов"

    l6 = [{"city": "Азов", "temperature": 30.0, "date": "2026-07-01"},
          {"city": "Аксай", "temperature": 30.0, "date": "2026-07-01"}]
    assert warmest_city(l6) == "Азов"

    l7 = [{"city": "Аксай", "temperature": 30.0, "date": "2026-07-01"},
          {"city": "Азов", "temperature": 30.0, "date": "2026-07-01"}]
    assert warmest_city(l7) == "Азов"
