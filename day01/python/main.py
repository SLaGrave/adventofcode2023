def clean_data(data: list) -> list:
    data = [line.strip() for line in data]

    return data


def part1(data: list) -> str:
    s = 0
    for line in data:
        first = None
        last = None
        for x in line:
            if x in "123456789":
                last = x
                if first is None:
                    first = x
        s += int(first+last)
    return s


def part2(data: list) -> str:
    s = 0
    for line2 in data:
        line = line2.replace("one", "o1e")
        line = line.replace("two", "t2o")
        line = line.replace("three", "t3e")
        line = line.replace("four", "f4r")
        line = line.replace("five", "f5e")
        line = line.replace("six", "s6x")
        line = line.replace("seven", "s7n")
        line = line.replace("eight", "e8t")
        line = line.replace("nine", "n9e")
        first = None
        last = None
        for x in line:
            if x in "123456789":
                last = x
                if first is None:
                    first = x
        s += int(first+last)
    return s



if __name__ == "__main__":
    with open("../input.txt", "r") as f:
        data = f.readlines()
    data = clean_data(data)
    p1 = part1(data)
    print(p1)
    p2 = part2(data)
    print(p2)
