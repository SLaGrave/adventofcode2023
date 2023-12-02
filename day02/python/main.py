maxes = {
    "red": 12,
    "green": 13,
    "blue": 14
}

def clean_data(data: list) -> list:
    data = [line.strip() for line in data]
    data2 = []
    for item in data:
        tmp = item.split(": ")
        idx = int(tmp[0].replace("Game ", ""))
        shows = [x.strip().split(", ") for x in tmp[1].split(";")]
        data2.append((idx, shows))
    return data2


def part1(data: list) -> str:
    s = 0
    # Logic goes here
    for item in data:
        shows = item[1]
        b = False
        for show in shows:
            for color in show:
                s1 = color.split(" ")
                if int(s1[0]) > maxes[s1[1]]:
                    s += item[0]
                    b = True
                    break
            if b: break
    return 5050 - s


def part2(data: list) -> str:
    s = 0
    # Logic goes here
    for game in data:
        shows = game[1]
        m = {"red": 0, "green": 0, "blue": 0}
        for show in shows:
            for color in show:
                s1 = color.split(" ")
                m[s1[1]] = max(m[s1[1]], int(s1[0]))
        s += m["red"] * m["green"] * m["blue"]
    return s


if __name__ == "__main__":
    with open("../input.txt", "r") as f:
        data = f.readlines()
    data = clean_data(data)
    p1 = part1(data)
    print(p1)
    p2 = part2(data)
    print(p2)
