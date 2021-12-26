use std::env;
use std::fs;
use std::fmt;

fn main() {
    let args: Vec<String> = env::args().collect();
    let filename = &args[1];
    let directions = fs::read_to_string(filename).expect("File cannot be read");

    let mut floor = 0;
    let mut first_basement = None;
    for (index, direction) in directions.chars().enumerate() {
        floor += match direction {
            '(' => 1,
            ')' => -1,
            _ => 0,
        };

        if floor < 0 && first_basement.is_none() {
            first_basement = Some(index + 1);
        }
    }

    println!("Part 1: {}", floor);
    let part_2 = match first_basement {
        None => "Directions never reach basement".to_string(),
        Some(index) => format!("{}", index)
    };
    println!("Part 2: {}", part_2)
}
