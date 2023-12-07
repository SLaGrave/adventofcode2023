def clean_data(data: list) -> list:
    data = [line.strip() for line in data]
    return data

def part1(data: list):
    total = 0
    # Logic goes here

    hands = list()
    for line in data:
        hand = line.split(" ")
        cards = hand[0]
        cards_scoring = str(hand[0])
        cards_scoring = cards_scoring.replace("T", "a")
        cards_scoring = cards_scoring.replace("J", "b")
        cards_scoring = cards_scoring.replace("Q", "c")
        cards_scoring = cards_scoring.replace("K", "d")
        cards_scoring = cards_scoring.replace("A", "e")
        bet = int(hand[1])
        type_dict = dict()
        for c in cards:
            if c not in type_dict.keys():
                type_dict[c] = 1
            else:
                type_dict[c] += 1
        # Hand type calc
        type_set = list(type_dict.values())
        type_set.sort()
        type_set.reverse()
        if type_set == [5]:
            t = 7
        elif type_set == [4,1]:
            t = 6
        elif type_set == [3,2]:
            t = 5
        elif type_set == [3,1,1]:
            t = 4
        elif type_set == [2,2,1]:
            t = 3
        elif type_set == [2,1,1,1]:
            t = 2
        else:
            t = 1
        hands.append((cards, bet, t, cards_scoring))
    hands.sort(key=lambda x: f"{x[2]}{x[3]}")

    for idx, hand in enumerate(hands):
        bet = hand[1]
        winnings = idx*bet + bet
        total += winnings

    return total


def part2(data: list):
    total = 0
    # Logic goes here

    hands = list()
    for line in data:
        hand = line.split(" ")
        cards = hand[0]
        cards_scoring = str(hand[0])
        cards_scoring = cards_scoring.replace("T", "a")
        cards_scoring = cards_scoring.replace("J", "0")
        cards_scoring = cards_scoring.replace("Q", "c")
        cards_scoring = cards_scoring.replace("K", "d")
        cards_scoring = cards_scoring.replace("A", "e")
        bet = int(hand[1])
        best_t = 0
        for replace in "23456789TQKA":
            new = cards.replace("J", replace)
            type_dict = dict()
            for c in new:
                if c not in type_dict.keys():
                    type_dict[c] = 1
                else:
                    type_dict[c] += 1
            # Hand type calc
            type_set = list(type_dict.values())
            type_set.sort()
            type_set.reverse()
            if type_set == [5]:
                t = 7
            elif type_set == [4,1]:
                t = 6
            elif type_set == [3,2]:
                t = 5
            elif type_set == [3,1,1]:
                t = 4
            elif type_set == [2,2,1]:
                t = 3
            elif type_set == [2,1,1,1]:
                t = 2
            else:
                t = 1
            best_t = max(best_t, t)
        hands.append((cards, bet, best_t, cards_scoring))
    hands.sort(key=lambda x: f"{x[2]}{x[3]}")

    for idx, hand in enumerate(hands):
        bet = hand[1]
        winnings = idx*bet + bet
        total += winnings
    
    return total


if __name__ == "__main__":
    with open("../input.txt", "r") as f:
        data = f.readlines()
    data = clean_data(data)
    p1 = part1(data)
    print(p1)
    p2 = part2(data)
    print(p2)
