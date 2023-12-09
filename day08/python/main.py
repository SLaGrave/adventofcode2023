import ast
import math

def clean_data(data: list) -> list:
    data = [line.strip() for line in data]
    
    nodes = dict()
    instructions = data[0]
    for i in range(len(data)-1):
        idx = i + 1
        line = data[idx]
        line = line.split(" = ")
        nodes[line[0]] = ast.literal_eval(line[1])

    return (instructions, nodes)


def part1(data: list):
    step = 0
    # Logic goes here
    instructions = data[0]
    nodes = data[1]
    current_node = "AAA"
    while current_node != "ZZZ":
        inst = instructions[step%len(instructions)]
        if inst == "R":
            current_node = nodes[current_node][1]
        else:
            current_node = nodes[current_node][0]
        step += 1
    return step


def part2(data: list):
    instructions = data[0]
    nodes = data[1]
    # Logic goes here
    current_nodes = [x for x in nodes.keys() if x[2]=="A"]
    steps = [0] * len(current_nodes)
    for idx in range(len(current_nodes)):
        while current_nodes[idx][2] != "Z":
            inst = instructions[steps[idx]%len(instructions)]
            if inst == "R":
                current_nodes[idx] = nodes[current_nodes[idx]][1]
            else:
                current_nodes[idx] = nodes[current_nodes[idx]][0]
            steps[idx] += 1
    total = 1
    for step in steps:
        total = math.lcm(total, step)
    return total


if __name__ == "__main__":
    with open("../input.txt", "r") as f:
        data = f.readlines()
    data = clean_data(data)
    p1 = part1(data)
    print(p1)
    p2 = part2(data)
    print(p2)
