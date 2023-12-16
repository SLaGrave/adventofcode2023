def clean_data(data: list) -> list:
    data = [line.strip() for line in data]
    # Logic goes here

    return data

def rotate_north(data) -> list:
    new_data = list()
    for x in range(len(data[0])):
        col = list()
        for y in range(len(data)):
            col.append(data[y][x])
        new_data.append(col)
    data = new_data

    flag = True
    while (flag):
        flag = False
        for idx, line in enumerate(data):
            for i in range(1, len(line)):
                if line[i-1] == "." and line[i] == "O":
                    data[idx][i-1] = "O"
                    data[idx][i] = "."
                    flag = True
    return data


def part1(data: list):
    total = 0
    # Logic goes here
    
    data = rotate_north(data)
    
    for line in data:
        for i in range(len(line)):
            if line[i] == "O":
                total += len(line)-i
    
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
