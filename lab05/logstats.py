LEVELS = ["DEBUG", "INFO", "WARNING", "ERROR"]
BROKEN_LEVEL = "BROKEN"

def parse_event(line: str) -> dict:
    if line.strip() == "":
        return {}
    segments = line.lstrip().split(None, 2)
    if len(segments) != 3 or segments[1] not in LEVELS:
        raise ValueError("Неверный формат строки")
    time, level, message = (s.strip() for s in segments)
    return {"time": time, "level": level, "message": message}

def count_levels(lines: list[str]) -> dict:
    result = dict()
    for line in lines:
        try:
            data = parse_event(line)
            result[data["level"]] = result.get(data["level"], 0) + 1
        except KeyError:
            continue
        except ValueError:
            result[BROKEN_LEVEL] = result.get(BROKEN_LEVEL, 0) + 1
    return result

def top_errors(lines: list[str], n: int) -> list[list]:
    result = dict()
    for line in lines:
        try:
            data = parse_event(line)
            if data["level"] == "ERROR":
                result[data["message"]] = result.get(data["message"], 0) + 1
        except ValueError:
            pass
    errors = sorted(result.items(), key=lambda pair: pair[0])
    errors = sorted(errors, key=lambda pair: pair[1], reverse=True)
    return [list(pair) for pair in errors[:n]]

def format_report(counts: dict, errors: list[list]) -> str:
    result = "Отчёт по журналу\n\n"
    sorted_levels = sorted(counts.items(), key= lambda x: x[0])
    for level in sorted_levels:
        result += level[0] + ": " + str(level[1]) + "\n"

    result += "\n"
    result += "Частые ошибки:\n"

    for error in errors:
        result += "- " + error[0] + " — " + str(error[1]) + "\n"

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
    data1_1 = ["", " ", "2026-03-01T09:03:55 INFO ok", "2026-03-01T09"]
    assert count_levels(data1_1) == {"INFO": 1, "BROKEN": 1}

    assert top_errors(data1, 1) == [["Нет доступа к каталогу /var/log", 2]]

    data2 = ["2026-03-02T10:00:00 ERROR Короткий запуск",
             "2026-03-02T10:00:30 ERROR Нет доступа к каталогу /var/log",
             "2026-03-02T10:01:00 ERROR Нет доступа к каталогу /var/log",
             "2026-03-02T10:02:00 ERROR Диск заполнен на 91%",
             "2026-03-02T10:02:00 ERROR Диск заполнен на 91%"]
    assert top_errors(data2, 2) == [["Диск заполнен на 91%", 2], ["Нет доступа к каталогу /var/log", 2]]

if __name__ == "__main__":
    main()
    #print("OK")