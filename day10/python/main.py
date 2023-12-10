from matplotlib.path import Path

def clean_data(data: list) -> list:
    data = [line.strip() for line in data]
    data = [list(x) for x in data]
    # Logic goes here

    return data

NORTH = (0, -1)
SOUTH = (0, 1)
EAST = (1, 0)
WEST = (-1, 0)

MAPPING = {
    "|": [NORTH, SOUTH],
    "-": [EAST, WEST],
    "L": [NORTH, EAST],
    "J": [NORTH, WEST],
    "7": [SOUTH, WEST],
    "F": [SOUTH, EAST],
}

PART2_MAPPING = {
    ('L', 'left'): 'up',
    ('F', 'up'): 'right',
    ('7', 'right'): 'down',
    ('J', 'down'): 'left',
    ('F', 'left'): 'down',
    ('7', 'up'): 'left',
    ('J', 'right'): 'up',
    ('L', 'down'): 'right',
    ('-', 'left'): 'left',
    ('-', 'right'): 'right',
    ('|', 'up'): 'up',
    ('|', 'down'): 'down',
}

REPLACE = "F"


def part1(data: list):
    # Logic goes here
    pipes = list()
    for y in range(len(data)):
        for x in range(len(data[0])):
            if data[y][x] == "S":
                pipes.append((x, y, REPLACE))
    for pipe in pipes:
        x = pipe[0]
        y = pipe[1]
        s = pipe[2]
        for angle in MAPPING[s]:
            newx = x+angle[0]
            newy = y+angle[1]
            try:
                news = data[newy][newx]
                if news == "S": news = REPLACE
                tmp = (newx, newy, news)
                if tmp not in pipes: pipes.append(tmp)
            except:
                pass
    return (int((len(pipes))/2), pipes)



def part2(data: list, pipes):
    total = 0
    # Logic goes here
    path = [x[0:2] for x in pipes]
    p = Path(path)
    for y in range(len(data)):
        for x in range(len(data[0])):
            if (x, y) not in path and p.contains_point((x, y)):
                total += 1
    return total


if __name__ == "__main__":
    with open("../input.txt", "r") as f:
        data = f.readlines()
    data = clean_data(data)
    p1, pipes = part1(data)
    print(p1)
    p2 = part2(data, pipes)
    print(p2)
