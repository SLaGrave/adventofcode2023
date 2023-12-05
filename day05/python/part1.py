import json
import math

def mapping_or_self(x, mapping):
    for s in mapping:
        dest_start = s[0]
        source_start = s[1]
        l = s[2]
        if x >= source_start and x <= source_start + l:
            return dest_start + (x-source_start)
    return x

def part1(data: list):
    lowest = math.inf
    # Logic goes here
    seeds = data["seeds"]
    
    mappings = ["seed-to-soil", "soil-to-fertilizer", "fertilizer-to-water", "water-to-light", "light-to-temperature", "temperature-to-humidity", "humidity-to-location"]

    for seed in seeds:
        tmp = seed
        for mapping in mappings:
            tmp = mapping_or_self(tmp, data[mapping])
        lowest = min(lowest, tmp)

    return lowest


if __name__ == "__main__":
    with open("../input_edited.json", "r") as f:
        data = json.loads(f.read())
    p1 = part1(data)
    print(p1)
