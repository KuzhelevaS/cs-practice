def parse_record(line: str) -> dict:
    if line.count(";") != 2:
        raise ValueError("wrong format")
    
    city, temp, date = line.split(";")
    if city == "" or date == "":
        raise ValueError("empty field")

    result = dict()
    result[city] = float(temp)
    return result


def read_valid(lines):
    result = []   
    for line in lines:
        if len(line) == 0:
            continue
        try:
            result.append(parse_record(line))
        except ValueError:
            print("невозможно обработать строку: \"{line}\"")
    return result

