def clean_data(data: list) -> list:
    data = [line.strip() for line in data]
    # Logic goes here

    return data


def part1(data: list):
    total = 0
    # Logic goes here

    return total


def part2(data: list):
    total = 0
    # Logic goes here
    
    return total


if __name__ == "__main__":
    with open("../input.txt", "r") as f:
        data = f.readlines()
    data = clean_data(data)
    p1 = part1(data)
    print(p1)
    p2 = part2(data)
    print(p2)
