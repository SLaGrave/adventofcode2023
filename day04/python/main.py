def clean_data(data: list) -> list:
    data = [line.strip() for line in data]
    data = [x.split(" | ") for x in data]
    # data = [[x[0].split(" "), x[1].split(" ")] for x in data]

    return data


def part1(data: list) -> str:
    s = 0
    # Logic goes here
    for card in data:
        winning = [int(q) for q in card[0].split(" ")]
        mine = [int(q) for q in card[1].split(" ")]
        total = 0
        for winning_num in winning:
            if winning_num in mine:
                if total == 0:
                    total = 1
                else:
                    total *= 2
        s += total
    return s

def score_card(winning, mine) -> int:
    total = 0
    for winning_num in winning:
        if winning_num in mine:
            total += 1
    return total

def part2(data: list) -> str:
    total = 0
    nums = [1] * len(data)
    for idx, value in enumerate(nums):
        card = data[idx]
        winning = [int(q) for q in card[0].split(" ")]
        mine = [int(q) for q in card[1].split(" ")]
        score = score_card(winning, mine)
        for i in range(score):
            nums[idx + i + 1] += value
        total += value
    return total


if __name__ == "__main__":
    with open("../edited_input.txt", "r") as f:
        data = f.readlines()
    data = clean_data(data)
    p1 = part1(data)
    print(p1)
    p2 = part2(data)
    print(p2)
