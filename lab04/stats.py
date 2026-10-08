def parse_record(line):
    if line.count(";") != 2:
        raise ValueError("wrong format")
    
    city, temp, date = line.split(";")
    if city == "" or date == "":
        raise ValueError("empty field")

    return city, float(temp)


def read_valid(lines):
    result = [] 
    err = 0  
    for line in lines:
        if len(line) == 0:
            continue
        try:
            result.append(parse_record(line))
        except ValueError:
            print("невозможно обработать строку: \"{line}\"")
            err += 1
            
    return result, err

def average_by_city(records):
    total = {}
    count = {}
    for city in records:
        total[city[0]] = total.get(city[0], 0) + city[1]
        count[city[0]] = count.get(city[0], 0) + 1
    result = dict()
    for city in total:
        result[city[0]] = city[1] / count.get(city[0])
    return result
