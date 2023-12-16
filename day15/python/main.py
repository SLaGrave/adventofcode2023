def clean_data(data: list) -> list:
    data = data[0].split(",")
    # Logic goes here

    return data

def hash_algo(s):
    curr = 0
    for c in s:
        a = ord(c)
        curr += a
        curr *= 17
        curr = curr%256
    return curr

def part1(data: list):
    total = 0
    # Logic goes here
    for s in data:
        total += hash_algo(s)
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
