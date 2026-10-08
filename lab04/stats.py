def parse_record(line: str) -> dict:
    if line.count(";") != 2:
        raise ValueError("wrong format")
    
    city, temp, date = line.split(";")
    if city == "" or date == "":
        raise ValueError("empty field")

    result = dict()
    result[city] = float(temp)
    return result


    

