use std::collections::HashMap;

struct Calibration {
    first_digit: u32, // Digits are used in part 1
    first_value: u32,
    last_digit: u32, // Values are used in part 2
    last_value: u32,
}

impl Calibration {
    fn new(original: String, mapping: &HashMap<&str, &str>) -> Calibration {
        // Create the modified string
        // Modded string has each value ("nine") replaced with the digit
        // + wrapped in the value ("nine9nine")
        let mut modified = original.clone();
        for (key, value) in mapping {
            modified = modified.replace(key, value);
        }

        // Get the digits properly
        let mut first_digit: u32 = 0;
        let mut first_value: u32 = 0;
        let mut last_digit: u32 = 0;
        let mut last_value: u32 = 0;
        // First digit in original string
        for c in original.chars() {
            if c.is_digit(10) {
                first_digit = c.to_digit(10).unwrap();
                break;
            }
        }
        // First digit in REVERSED original string
        for c in original.chars().rev() {
            if c.is_digit(10) {
                last_digit = c.to_digit(10).unwrap();
                break;
            }
        }
        // Likewise for the modified string
        for c in modified.chars() {
            if c.is_digit(10) {
                first_value = c.to_digit(10).unwrap();
                break;
            }
        }
        for c in modified.chars().rev() {
            if c.is_digit(10) {
                last_value = c.to_digit(10).unwrap();
                break;
            }
        }

        Calibration {
            first_digit,
            first_value,
            last_digit,
            last_value,
        }
    }

    fn get_part1(&self) -> u32 {
        self.first_digit * 10 + self.last_digit
    }

    fn get_part2(&self) -> u32 {
        self.first_value * 10 + self.last_value
    }
}

fn main() {
    let value_mapping = HashMap::from([
        ("one", "one1one"),
        ("two", "two2two"),
        ("three", "three3three"),
        ("four", "four4four"),
        ("five", "five5five"),
        ("six", "six6six"),
        ("seven", "seven7seven"),
        ("eight", "eight8eight"),
        ("nine", "nine9nine"),
    ]);

    let input = include_str!("../../input.txt");
    let lines: Vec<&str> = input.split("\r\n").collect();
    let mut calibrations: Vec<Calibration> = Vec::new();
    for line in lines {
        calibrations.push(Calibration::new(line.to_string(), &value_mapping));
    }
    let mut part1 = 0;
    calibrations.iter().for_each(|x| {
        part1 += x.get_part1();
    });
    let mut part2 = 0;
    calibrations.iter().for_each(|x| {
        part2 += x.get_part2();
    });
    dbg!(part1, part2);
}
