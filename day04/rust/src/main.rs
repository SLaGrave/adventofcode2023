fn str_to_i32(s: &str) -> i32 {
    s.to_string().parse::<i32>().unwrap()
}

#[derive(Debug)]
struct Card {
    winning_nums: Vec<i32>,
    my_nums: Vec<i32>,
}

impl Card {
    fn new(wins: &String, mine: &String) -> Card {
        let winning_nums: Vec<i32> = wins.split(" ").map(|x| str_to_i32(x)).collect();
        let my_nums: Vec<i32> = mine.split(" ").map(|x| str_to_i32(x)).collect();
        Card {
            winning_nums,
            my_nums,
        }
    }

    fn part1_score(&self) -> i32 {
        let mut total: i32 = 0;
        for w in &self.winning_nums {
            for m in &self.my_nums {
                if w == m {
                    if total == 0 {
                        total = 1;
                    } else {
                        total *= 2;
                    }
                    break;
                }
            }
        }
        return total;
    }

    fn part2_score(&self) -> i32 {
        let mut total: i32 = 0;
        for w in &self.winning_nums {
            for m in &self.my_nums {
                if w == m {
                    total += 1;
                    break;
                }
            }
        }
        return total;
    }
}

fn main() {
    let input = include_str!("../../edited_rust_input.txt");
    let lines: Vec<String> = input.split("\n").map(|x| x.to_string()).collect();

    let mut cards: Vec<Card> = Vec::new();

    for i in 0..lines.len() {
        // If it's even
        if i % 2 == 0 {
            // Create a new card
            cards.push(Card::new(lines.get(i).unwrap(), lines.get(i+1).unwrap()));
        }
    }

    let mut part1: i32 = 0;
    for card in &cards {
        part1 += card.part1_score();
    }
    dbg!(part1);

    // Make a vector of all ones
    let mut cards_held: Vec<i32> = Vec::new();
    for _ in 0..cards.len() {
        cards_held.push(1);
    }
    for i in 0..cards.len() {
        let num_held = cards_held.get(i).unwrap().clone();
        let score = cards.get(i).unwrap().part2_score();
        for xy in 0..score {
            let idx = i + xy as usize + 1;
            let new_value = cards_held.get(idx).unwrap() + num_held;
            cards_held[idx] = new_value;
        }
    }
    dbg!(cards_held.iter().sum::<i32>());
}
