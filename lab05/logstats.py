levels = ["DEBUG", "INFO", "WARNING", "ERROR"]

def parse_event(line: str) -> dict:
    if line.strip() == "":
        return {}
    time, level, message = map(str.strip, line.lstrip().split(None, 2))
    if not level in levels:
        raise ValueError("Неверный формат строки")
    return {"time": time, "level": level, "message": message}

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
    assert ks_catch_exception(parse_event, "поломанная строка") is ValueError
    assert ks_catch_exception(parse_event, "поломанная") is ValueError
    assert parse_event("") == dict()
if __name__ == "__main__":
    main()
    print("OK")