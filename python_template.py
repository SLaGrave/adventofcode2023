def clean_data(data: list) -> list:
    data = [line.strip() for line in data]
    # Logic goes here

    return data


def part1(data: list) -> str:
    s = ""
    # Logic goes here

    return s


def part2(data: list) -> str:
    s = ""
    # Logic goes here
    
    return s


if __name__ == "__main__":
    with open("../input.txt", "r") as f:
        data = f.readlines()
    data = clean_data(data)
    p1 = part1(data)
    print(p1)
    p2 = part2(data)
    print(p2)
