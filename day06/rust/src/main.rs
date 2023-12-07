fn does_this_win(held: i64, time: i64, distance: i64) -> bool {
    let time_to_go = time - held;
    held * time_to_go > distance
}

#[derive(Debug)]
struct Race {
    time: i64,
    distance: i64,
}

impl Race {
    fn new(time: i64, distance: i64) -> Race {
        Race { time, distance }
    }

    fn ways_to_win(&self) -> i64 {
        let mut ways_to_win: i64 = 0;
        let mut held: i64 = 0;
        while held <= self.time {
            if does_this_win(held, self.time, self.distance) {
                ways_to_win += 1;
            }
            held += 1;
        }
        ways_to_win
    }
}

fn main() {
    let part1_input = Vec::from([
        Race::new(34, 204),
        Race::new(90, 1713),
        Race::new(89, 1210),
        Race::new(86, 1780),
    ]);
    let part2_input = Race::new(34908986, 204171312101780);

    let mut part1: i64 = 1;
    for race in part1_input {
        part1 *= race.ways_to_win();
    }
    dbg!(part1);

    let part2 = part2_input.ways_to_win();
    dbg!(part2);
}
