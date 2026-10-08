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