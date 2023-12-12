import ast
import functools

######################################################
# Parse Data
######################################################
def clean_data(data: list) -> list:
    data = [line.strip() for line in data]
    new_data = list()
    for line in data:
        line = line.split(" ")
        s = line[0]
        v = ast.literal_eval(f"[{line[1]}]")
        new_data.append([s, v])

    return new_data

def clean_data2(data: list) -> list:
    data = [line.strip() for line in data]
    new_data = list()
    for line in data:
        line = line.split(" ")
        s = line[0]
        v = ast.literal_eval(f"[{line[1]}]")
        s2 = [s]*5
        v2 = []
        for _ in range(5):
            v2.extend(v)
        new_data.append(["?".join(s2), v2])

    return new_data

######################################################
# Part 1
######################################################
def make_strings(s, v):
    if set(s) == set('.#'):
        if does_string_match(s, v):
            return 1
        return 0
    else:
        total = 0
        for idx, c in enumerate(s):
            if c == '?':
                total += make_strings(f"{s[:idx]}#{s[idx+1:]}", v)
                total += make_strings(f"{s[:idx]}.{s[idx+1:]}", v)
                break
        return total

def does_string_match(s, v):
    correct_str = ""
    for value in v:
        correct_str += "#"*value
        correct_str += "."
    correct_str = correct_str[:-1]

    # Remove unneed periods
    while True:
        removed = s.replace("..", ".")
        if removed == s:
            break
        s = removed
    # remove starting/ending .
    if s[0] == ".": s = s[1:]
    if s[-1] == ".": s = s[:-1]

    return s == correct_str


def part1(data: list):
    total = 0
    # Logic goes here
    for idx, line in enumerate(data):
        print(f"Line {idx}/{len(data)}")
        total += make_strings(*line)
    return total


######################################################
# Part 2
######################################################
@functools.cache
def recursive_part2(s, v):
    # If we have no more values to check
    if len(v) == 0:
        # And there's still an error which hasn't been handled
        if "#" in s:
            return 0
        return 1

    # The current chunck of errors we're dealing with
    current_chunk = v[0]
    total = 0

    # The chunk we're looking at will start at zero and 
    # go up to the largest index where we can fit all other chunks
    for start in range(len(s) - current_chunk - sum(v[1:]) - (len(v[1:])-1)):
        for end in range(start, start + current_chunk):
            if end > 0 and start == end and s[end-1] == "#":
                return total
            if end >= len(s):
                return total
            if s[end] == ".":
                break
            if end == start + current_chunk - 1:
                if end + 1 < len(s) and s[end+1] == "#":
                    break
                total += recursive_part2(s[end+2:], v[1:])
    return total

def part2(data: list):
    total = 0
    # Logic goes here
    for idx, line in enumerate(data):
        total += recursive_part2(line[0], tuple(line[1]))
    return total


if __name__ == "__main__":
    with open("../input.txt", "r") as f:
        data = f.readlines()
    data1 = clean_data(data)
    # p1 = part1(data1)
    # print(p1)
    data2 = clean_data2(data)
    p2 = part2(data2)
    print(p2)
