def clean_data(data: list) -> list:
    data = [line.strip() for line in data]
    data = [[int(x) for x in y.split(" ")] for y in data]
    # Logic goes here

    return data


def part1(data: list):
    total = 0
    # Logic goes here
    for x in data:
        history = [x]
        while True:
            last = history[-1]
            if set(last) == {0}: break
            newest = list()
            for i in range(len(last)-1):
                newest.append(last[i+1] - last[i])
            history.append(newest)
        for i in range(len(history)):
            real = -1-i
            if real == -1:
                history[real].append(0)
            else:
                history[real].append(history[real][-1]+history[real+1][-1])
        total += history[0][-1] 
    return total


def part2(data: list):
    total = 0
    # Logic goes here
    for x in data:
        history = [list(reversed(x))]
        while True:
            last = history[-1]
            if set(last) == {0}: break
            newest = list()
            for i in range(len(last)-1):
                newest.append(last[i+1] - last[i])
            history.append(newest)
        for i in range(len(history)):
            real = -1-i
            if real == -1:
                history[real].append(0)
            else:
                history[real].append(history[real][-1]+history[real+1][-1])
        total += history[0][-1] 
    return total


if __name__ == "__main__":
    with open("../input.txt", "r") as f:
        data = f.readlines()
    data = clean_data(data)
    p1 = part1(data)
    print(p1)
    p2 = part2(data)
    print(p2)
