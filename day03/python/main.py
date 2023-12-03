def clean_data(data: list) -> list:
    data = [line.strip() for line in data]
    # Logic goes here

    return data


def check_value(value, data, x, y):
    if value == "": return 0
    v = int(value)
    minus = len(value)+1
    for vy in range(-1, 2):
        for vx in range(-minus, 1):
            if is_symbol(data, x + vx, y + vy):
                return v
    return 0


def is_symbol(data, x, y):
    if y < 0 or y >= len(data):
        return False
    if x < 0 or x >= len(data[y]):
        return False
    return data[y][x] not in "0123456789" and data[y][x] != "."


def part1(data: list) -> str:
    s = 0
    # Logic goes here
    y = 0
    while True:
        x = 0
        value = ""
        while x < len(data[y]):
            if data[y][x] == ".":
                s += check_value(value, data, x, y)
                value = ""
                x += 1
                continue
            if data[y][x] not in "0123456789":
                s += check_value(value, data, x, y)
                value = ""
                x += 1
                continue
            value += data[y][x]
            x += 1
        s += check_value(value, data, x,y)

        y += 1
        if y == len(data): break

    return s

def is_symbol2(data, x, y):
    if y < 0 or y >= len(data):
        return False
    if x < 0 or x >= len(data[y]):
        return False
    if data[y][x] not in "0123456789" and data[y][x] != ".":
        return data[y][x]
    return False

def check_value2(value, data, x, y):
    umm = list()
    if value == "": return 0
    v = int(value)
    minus = len(value)+1
    for vy in range(-1, 2):
        for vx in range(-minus, 1):
            yuck = is_symbol2(data, x + vx, y + vy)
            if yuck != False:
                umm.append( (v, (yuck, x+vx, y+vy)))
    if umm == []:
        return 0
    return umm


def part2(data: list) -> str:
    s = 0
    # Logic goes here
    gears = list()
    y = 0
    while True:
        x = 0
        value = ""
        while x < len(data[y]):
            if data[y][x] == ".":
                tmp = check_value2(value, data, x, y)
                if tmp != 0:
                    gears.append(*tmp)
                value = ""
                x += 1
                continue
            if data[y][x] not in "0123456789":
                tmp = check_value2(value, data, x, y)
                if tmp != 0:
                    gears.append(*tmp)
                value = ""
                x += 1
                continue
            value += data[y][x]
            x += 1
        tmp = check_value2(value, data, x,y)
        if tmp != 0:
            gears.append(*tmp)

        y += 1
        if y == len(data): break

    for y in range(len(data)):
        for x in range(len(data[y])):
            g = [q for q in gears if q[1][1] == x and q[1][2] == y]
            if len(g) == 2:
                s += g[0][0] * g[1][0]
    return s


if __name__ == "__main__":
    with open("../input.txt", "r") as f:
        data = f.readlines()
    data = clean_data(data)
    p1 = part1(data)
    print(p1)
    p2 = part2(data)
    print(p2)
