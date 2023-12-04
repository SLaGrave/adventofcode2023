#[derive(Debug, PartialEq)]
struct PartLocation {
    x: i32,
    y: i32,
}

impl PartLocation {
    fn new(x: i32, y: i32) -> PartLocation {
        PartLocation { x, y }
    }
}

#[derive(Debug)]
struct PartNumber {
    value: i32,
    adjacent_locations: Vec<PartLocation>,
}

impl PartNumber {
    fn new(s: String, x: i32, y: i32) -> PartNumber {
        let value: i32 = s.parse().unwrap();

        let l = s.len();
        let mut adjacent_locations: Vec<PartLocation> = Vec::new();
        for vy in -1..2 as i32 {
            for vx in -1 - l as i32..1 as i32 {
                adjacent_locations.push(PartLocation::new(x + vx, y + vy));
            }
        }
        PartNumber {
            value,
            adjacent_locations,
        }
    }
}

#[derive(Debug, PartialEq)]
enum PartKind {
    NoOp,
    Gear,
    NonGear,
}

#[derive(Debug)]
struct Part {
    kind: PartKind,
    location: PartLocation,
}

impl Part {
    fn new(c: char, x: i32, y: i32) -> Part {
        let kind: PartKind = match c {
            '.' => PartKind::NoOp,
            '*' => PartKind::Gear,
            _ => PartKind::NonGear,
        };
        Part {
            kind,
            location: PartLocation::new(x, y),
        }
    }
}

fn main() {
    let input = include_str!("../../input.txt");
    let lines: Vec<String> = input.split("\r\n").map(|x| x.to_string()).collect();

    let mut parts: Vec<Part> = Vec::new();
    let mut part_nums: Vec<PartNumber> = Vec::new();

    for y in 0..lines.len() {
        let mut row = lines.get(y).unwrap().chars();
        let mut tmp: String = "".to_string();
        for x in 0..row.clone().count() {
            let c = row.next().unwrap();
            match c {
                '0' | '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9' => {
                    tmp.push(c);
                }
                _ => {
                    if tmp != "".to_string() {
                        part_nums.push(PartNumber::new(tmp, x as i32, y as i32));
                    }
                    tmp = "".to_string();
                    parts.push(Part::new(c, x as i32, y as i32));
                }
            }
        }
    }

    let mut part1: i32 = 0;
    for part_num in &part_nums {
        let mut is_valid = false;
        for part in &parts {
            if part.kind != PartKind::NoOp && part_num.adjacent_locations.contains(&part.location) {
                is_valid = true;
                break;
            }
        }
        if is_valid {
            part1 += part_num.value;
        }
    }
    dbg!(part1);

    let mut part2: i32 = 0;
    for part in &parts {
        if part.kind != PartKind::Gear {
            continue;
        }
        let mut adj_numbers: Vec<i32> = Vec::new();
        for part_num in &part_nums {
            if part_num.adjacent_locations.contains(&part.location) {
                adj_numbers.push(part_num.value);
            }
        }
        if adj_numbers.len() == 2 {
            part2 += adj_numbers.get(0).unwrap() * adj_numbers.get(1).unwrap();
        }
    }
    dbg!(part2);
}
