LEVELS = ["DEBUG", "INFO", "WARNING", "ERROR"]
BROKEN_LEVEL = "BROKEN"

def parse_event(line: str) -> dict:
    if line.strip() == "":
        return {}
    time, level, message = map(str.strip, line.lstrip().split(None, 2))
    if not level in LEVELS:
        raise ValueError("Неверный формат строки")
    return {"time": time, "level": level, "message": message}

def count_levels(lines: list[str]) -> dict:
    result = dict()
    for line in lines:
        try:
            data = parse_event(line)
            result[data["level"]] = result.get(data["level"], 0) + 1
        except ValueError:
            result[BROKEN_LEVEL] = result.get(BROKEN_LEVEL, 0) + 1
    return result

def ks_catch_exception(method, arg):
    try:
        method(arg)
    except Exception as e:
        return e.__class__

def main():
    assert parse_event("2026-03-01T09:03:55 ERROR Не удалось открыть файл data.csv") \
        == {"time": "2026-03-01T09:03:55", "level": "ERROR", "message": "Не удалось открыть файл data.csv"}
    assert parse_event("2026-03-01T09:03:55 INFO Не удалось открыть файл data.csv") \
           == {"time": "2026-03-01T09:03:55", "level": "INFO", "message": "Не удалось открыть файл data.csv"}
    assert parse_event("2026-03-01T09:03:55 WARNING Не удалось открыть файл data.csv") \
           == {"time": "2026-03-01T09:03:55", "level": "WARNING", "message": "Не удалось открыть файл data.csv"}
    assert parse_event("2026-03-01T09:03:55 DEBUG Не удалось открыть файл data.csv") \
           == {"time": "2026-03-01T09:03:55", "level": "DEBUG", "message": "Не удалось открыть файл data.csv"}
    assert parse_event(" 2026-03-01T09:03:55 ERROR Не удалось открыть файл data.csv") \
           == {"time": "2026-03-01T09:03:55", "level": "ERROR", "message": "Не удалось открыть файл data.csv"}
    assert ks_catch_exception(parse_event, "поломанная строка") is ValueError
    assert ks_catch_exception(parse_event, "поломанная") is ValueError
    assert parse_event("") == dict()

    data1 = ["2026-03-02T10:00:00 INFO Короткий запуск",
            "2026-03-02T10:00:30 ERROR Нет доступа к каталогу /var/log",
            "2026-03-02T10:01:00 ERROR Нет доступа к каталогу /var/log",
            "2026-03-02T10:02:00 WARNING Диск заполнен на 91%",
            "2026-03-02T10:02:00 SOMEELSE Диск заполнен на 91%"]

    assert count_levels(data1) == {BROKEN_LEVEL: 1, "ERROR": 2, "INFO": 1, "WARNING": 1}


if __name__ == "__main__":
    main()
    #print("OK")