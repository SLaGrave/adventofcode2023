use regex::Regex;

#[derive(Debug)]
struct Game {
    game_no: i32,
    largest_red: i32,
    largest_green: i32,
    largest_blue: i32,
}

impl Game {
    fn new(description: &str) -> Game {
        // Game_no
        let re_game_no = Regex::new(r"Game (?<game_no>[0-9]+)").unwrap();
        let caps_game_no = re_game_no.captures(description).unwrap();
        let game_no = str_to_i32(&caps_game_no["game_no"]);

        // Largest_red
        let re_reds = Regex::new(r"(?<num>[0-9]+) red").unwrap();
        let red_strs: Vec<&str> = re_reds
            .captures_iter(description)
            .map(|m| m.name("num").unwrap().as_str())
            .collect();
        let mut reds: Vec<i32> = Vec::new();
        for s in red_strs {
            reds.push(str_to_i32(s));
        }
        let largest_red: i32 = *reds.iter().max().unwrap_or(&0);

        // Largest_green
        let re_greens = Regex::new(r"(?<num>[0-9]+) green").unwrap();
        let green_strs: Vec<&str> = re_greens
            .captures_iter(description)
            .map(|m| m.name("num").unwrap().as_str())
            .collect();
        let mut greens: Vec<i32> = Vec::new();
        for s in green_strs {
            greens.push(str_to_i32(s));
        }
        let largest_green: i32 = *greens.iter().max().unwrap_or(&0);

        // Largest_blue
        let re_blues = Regex::new(r"(?<num>[0-9]+) blue").unwrap();
        let blue_strs: Vec<&str> = re_blues
            .captures_iter(description)
            .map(|m| m.name("num").unwrap().as_str())
            .collect();
        let mut blues: Vec<i32> = Vec::new();
        for s in blue_strs {
            blues.push(str_to_i32(s));
        }
        let largest_blue: i32 = *blues.iter().max().unwrap_or(&0);

        Game {
            game_no,
            largest_red,
            largest_green,
            largest_blue,
        }
    }

    fn legal(&self, red: i32, green: i32, blue: i32) -> bool {
        !(self.largest_red > red || self.largest_green > green || self.largest_blue > blue)
    }
}

fn str_to_i32(s: &str) -> i32 {
    s.to_string().parse::<i32>().unwrap()
}

fn main() {
    let input = include_str!("../../input.txt");
    let lines: Vec<&str> = input.split("\r\n").collect();

    let mut games: Vec<Game> = Vec::new();
    for line in lines {
        games.push(Game::new(line));
    }

    let mut part1: i32 = 0;
    let mut part2: i32 = 0;

    for game in games {
        if game.legal(12, 13, 14) {
            part1 += game.game_no;
        }
        part2 += game.largest_red * game.largest_green * game.largest_blue
    }

    dbg!(&part1, &part2);
}
