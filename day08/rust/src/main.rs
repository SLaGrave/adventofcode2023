use serde::{Deserialize, Serialize};

#[derive(Debug, Deserialize, Serialize)]
struct Day08 {
    instructions: String,
    nodes: Vec<Node>,
}

impl Day08 {
    fn get_node(&self, name: String) -> Option<&Node> {
        for node in &self.nodes {
            if node.name == name {
                return Option::Some(node);
            }
        }
        return Option::None;
    }

    fn get_instruction(&self, idx: i64) -> LeftRightType {
        let real_idx: i64 = idx % (self.instructions.len() as i64);
        if self.instructions.chars().nth(real_idx as usize).unwrap() == 'L' {
            return LeftRightType::LEFT;
        } else {
            return LeftRightType::RIGHT;
        }
    }
}

#[derive(Debug, Deserialize, Serialize)]
struct Node {
    name: String,
    lr: LeftRight,
}

impl Node {
    fn is_part1_end(&self) -> bool {
        self.name == "ZZZ".to_string()
    }

    fn is_part2_begin(&self) -> bool {
        self.name.chars().nth(2).unwrap() == 'A'
    }

    fn is_part2_end(&self) -> bool {
        self.name.chars().nth(2).unwrap() == 'Z'
    }
}

enum LeftRightType {
    LEFT,
    RIGHT,
}

#[derive(Debug, Deserialize, Serialize)]
struct LeftRight {
    left: String,
    right: String,
}

fn lcm(first: i64, second: i64) -> i64 {
    first * second / gcd(first, second)
}

fn gcd(first: i64, second: i64) -> i64 {
    let mut max = first;
    let mut min = second;
    if min > max {
        let val = max;
        max = min;
        min = val;
    }

    loop {
        let res = max % min;
        if res == 0 {
            return min;
        }

        max = min;
        min = res;
    }
}

fn main() {
    let input_str = include_str!("../../input.ron");
    let input: Day08 = ron::from_str(input_str).unwrap();

    // Part one
    let mut part1: i64 = 0;
    let mut current_node: &Node = input.get_node("AAA".to_string()).unwrap();
    while !current_node.is_part1_end() {
        let t = input.get_instruction(part1);
        match t {
            LeftRightType::LEFT => {
                current_node = input.get_node(current_node.lr.left.clone()).unwrap();
            }
            LeftRightType::RIGHT => {
                current_node = input.get_node(current_node.lr.right.clone()).unwrap();
            }
        }
        part1 += 1;
    }
    dbg!(part1);

    // Part two
    let mut cycle_lengths: Vec<i64> = Vec::new();
    for node in &input.nodes {
        if node.is_part2_begin() {
            let mut count: i64 = 0;
            let mut current_node = node;
            while !current_node.is_part2_end() {
                let t = input.get_instruction(count);
                match t {
                    LeftRightType::LEFT => {
                        current_node = input.get_node(current_node.lr.left.clone()).unwrap();
                    }
                    LeftRightType::RIGHT => {
                        current_node = input.get_node(current_node.lr.right.clone()).unwrap();
                    }
                }
                count += 1;
            }
            cycle_lengths.push(count);
        }
    }
    let mut part2: i64 = 1;
    for cycle_length in cycle_lengths {
        part2 = lcm(part2, cycle_length);
    }
    dbg!(part2);
}
