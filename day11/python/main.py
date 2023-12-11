
def clean_data(data: list) -> list:
    data = [line.strip() for line in data]
    int_data = list()
    for x in range(len(data[0])):
        if x == 0:
            flag = True
            for y in range(len(data)):
                int_data.append(data[y][x])
                if data[y][x] == "#": flag = False
            if flag:
                for y in range(len(data)):
                    int_data[y] += data[y][x]
        else:
            flag = True
            for y in range(len(data)):
                int_data[y] += data[y][x]
                if data[y][x] == "#": flag = False
            if flag:
                for y in range(len(data)):
                    int_data[y] += data[y][x]

    new_data = list()
    for line in int_data:
        new_data.append(line)
        if set(line) == {'.'}:
            new_data.append(line)

    return new_data

def clean_data2(data: list) -> list:
    data = [line.strip() for line in data]
    empty_cols = list()
    empty_rows = list()
    for x in range(len(data[0])):
        col = list()
        for y in range(len(data)):
            col.append(data[y][x])
        if set(col) == {'.'}: empty_cols.append(x)
    for y in range(len(data)):
        if set(data[y]) == {'.'}: empty_rows.append(y)

    return (data, empty_cols, empty_rows)

def dist(x1, y1, x2, y2):
    return abs(x2-x1) + abs(y2-y1)

def part1(data: list):
    total = 0
    # Logic goes here
    galaxies = list()
    for y in range(len(data)):
        for x in range(len(data[0])):
            if data[y][x] == "#":
                galaxies.append((x, y))
    checked = list()
    for idx, galaxy1 in enumerate(galaxies):
        print(f"Galaxy {idx}/{len(galaxies)}")
        for galaxy2 in galaxies:
            if galaxy1 == galaxy2: continue
            if {galaxy1, galaxy2} not in checked:
                checked.append({galaxy1, galaxy2})
                total+=dist(galaxy1[0], galaxy1[1], galaxy2[0], galaxy2[1])
    return total

def is_between(q, i1, i2):
    return (q < i1 and q > i2) or (q > i1 and q < i2)

MULTIPLIER = 1000000

def part2(data: list):
    total = 0
    # Logic goes here
    grid = data[0]
    empty_cols = data[1]
    empty_rows = data[2]
    data = grid
    galaxies = list()
    for y in range(len(data)):
        for x in range(len(data[0])):
            if data[y][x] == "#":
                galaxies.append((x, y))
    checked = list()
    for idx, galaxy1 in enumerate(galaxies):
        print(f"Galaxy {idx}/{len(galaxies)}")
        for galaxy2 in galaxies:
            if galaxy1 == galaxy2: continue
            if {galaxy1, galaxy2} not in checked:
                checked.append({galaxy1, galaxy2})
                d=dist(galaxy1[0], galaxy1[1], galaxy2[0], galaxy2[1])
                for row in empty_rows:
                    if is_between(row, galaxy1[1], galaxy2[1]):
                        d += (MULTIPLIER-1)
                for col in empty_cols:
                    if is_between(col, galaxy1[0], galaxy2[0]):
                        d += (MULTIPLIER-1)
                total += d
    return total


if __name__ == "__main__":
    with open("../input.txt", "r") as f:
        data = f.readlines()
    # data1 = clean_data(data)
    # p1 = part1(data1)
    # print(p1)
    data2 = clean_data2(data)
    p2 = part2(data2)
    print(p2)
