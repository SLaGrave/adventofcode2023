import json
import math

def mapping_or_self(x, mapping):
    for s in mapping:
        dest_start = s[1]
        source_start = s[0]
        l = s[2]
        if x >= source_start and x <= source_start + l:
            return dest_start + (x-source_start)
    return x

def is_in_range(seed, ranges):
    for r in ranges:
        if seed >= r[0] and seed <= r[0] + r[1]:
            return True
    return False 

def part2(data):
    print("test")
    # Logic goes here
    seed_ranges = data["seeds"]
    i = 0
    seeds = list()
    while i < len(seed_ranges):
        start = seed_ranges[i]
        l = seed_ranges[i+1]
        seeds.append((start, l))
        i += 2
    
    mappings = ["seed-to-soil", "soil-to-fertilizer", "fertilizer-to-water", "water-to-light", "light-to-temperature", "temperature-to-humidity", "humidity-to-location"]
    mappings.reverse()

    lowest = 48501810

    while True:
        print(lowest)
        tmp = lowest
        for mapping in mappings:
            tmp = mapping_or_self(tmp, data[mapping])
        if is_in_range(tmp, seeds):
            return lowest
        lowest += 1


if __name__ == "__main__":
    with open("../input_edited.json", "r") as f:
        data = json.loads(f.read())
    p2 = part2(data)
    print(p2)
