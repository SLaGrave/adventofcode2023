
## Test data
# data = [(7, 9), (15, 40), (30, 200)]
## Part 1
# data = [(34, 204), (90, 1713), (89, 1210), (86, 1780)]
# Part 2
data = [(34908986, 204171312101780)]

def part1():
    # wins = [0, 0, 0]
    # wins = [0, 0, 0, 0]
    wins = [0]
    # Logic goes here
    for idx, race in enumerate(data):
        time = 0
        while time <= race[0]:
            dist = (race[0]-time)*time
            if dist > race[1]:
                wins[idx] += 1
            time += 1

    # return wins[0] * wins[1] * wins[2]
    # return wins[0] * wins[1] * wins[2] * wins[3]
    return wins[0]



if __name__ == "__main__":
    p1 = part1()
    print(p1)

