use std::{env, fs, collections};

fn visited_houses(directions: &str, no_of_santas:usize) -> usize {
    let mut houses = collections::HashMap::new();
    let vectors = collections::HashMap::from([
        ("^", (0, 1)),
        (">", (1, 0)),
        ("v", (0, -1)),
        ("<", (-1, 0))
    ]);

    let mut santa_pos = Vec::new();
    for _ in 0..no_of_santas {
        santa_pos.push((0, 0))
    }

    houses.insert(santa_pos[0], 3);

    for santa in 0..no_of_santas {
        for direction in directions.chars().collect::<Vec<char>>()[santa..].iter().step_by(no_of_santas) {
            let (x, y) = vectors.get(direction.to_string().as_str()).unwrap();
            santa_pos[santa] = (santa_pos[santa].0 + x, santa_pos[santa].1 + y);
            let house = houses.entry(santa_pos[santa]).or_insert(0);
            *house += 1;
        }
    }

    return houses.len();
}

fn main() {

    let args: Vec<String> = env::args().collect();
    let filename = &args[1];
    let directions = fs::read_to_string(filename).expect("File cannot be read");
    println!("Part 1: {}", visited_houses(&directions, 1));
    println!("Part 2: {}", visited_houses(&directions, 2));

}

