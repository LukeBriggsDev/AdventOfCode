use std::{env, fs};
use fancy_regex::Regex;

enum Operation {
    Toggle,
    TurnOn,
    TurnOff
}

struct Instruction {
    top_left: [usize; 2],
    bottom_right: [usize; 2],
    operation: Operation
}

/// Returns parsed instructions from given input
fn parse_input(instructions: &str) -> Vec<Instruction> {
    let instructions = instructions.split('\n');
    let re = Regex::new(r"\d+,*\d*").unwrap();
    let mut parsed_instructions = Vec::new();
    for instruction in instructions {
        let result = re.find_iter(instruction);

        let mut top_left = [0, 0];
        let mut bottom_right = [0, 0];

        for (pos, group) in result.enumerate() {
            let parts = group.unwrap().as_str().split(",");
            if pos == 0 {
                for i in 0..2 {
                    top_left[i] = parts.clone().collect::<Vec<&str>>()[i].parse::<usize>().unwrap();
                }
            }
            else if pos == 1 {
                for i in 0..2 {
                    bottom_right[i] = parts.clone().collect::<Vec<&str>>()[i].parse::<usize>().unwrap();
                }
            }
        }

        let operation :Operation;

        if instruction.starts_with("turn on") {
            operation = Operation::TurnOn
        }
        else if instruction.starts_with("turn off") {
            operation = Operation::TurnOff
        }
        else {
            operation = Operation::Toggle
        }
        parsed_instructions.push(Instruction {top_left, bottom_right, operation})
    }
    return parsed_instructions;
}

fn part_1 (instructions: &Vec<Instruction>) -> usize {

    let mut lights = [[false; 1000]; 1000];

    for instruction in instructions {
        for x in instruction.top_left[0]..instruction.bottom_right[0]+1 {
            for y in instruction.top_left[1]..instruction.bottom_right[1]+1 {
                match instruction.operation {
                    Operation::TurnOn => lights[y][x] = true,
                    Operation::TurnOff => lights[y][x] = false,
                    Operation::Toggle => lights[y][x] = !lights[y][x]
                }
            }
        }
    }

    let mut count = 0;
    for row in 0..1000 {
        for col in 0..1000 {
            if lights[row][col]{
                count += 1;
            }
        }
    }

    return count
}

fn part_2(instructions: &Vec<Instruction>) -> usize {
    let mut lights = [[0usize; 1000]; 1000];

    for instruction in instructions {
        for x in instruction.top_left[0]..instruction.bottom_right[0]+1 {
            for y in instruction.top_left[1]..instruction.bottom_right[1]+1 {
                match instruction.operation {
                    Operation::TurnOn => lights[y][x] += 1,
                    Operation::TurnOff => lights[y][x] -= if lights[y][x] == 0 {0} else {1},
                    Operation::Toggle => lights[y][x] += 2
                }
            }
        }
    }

    let mut count = 0;
    for row in 0..1000 {
        for col in 0..1000 {
            count += lights[row][col];
        }
    }

    return count
}

fn main() {
    let args: Vec<String> = env::args().collect();
    let filename = &args[1];
    let instructions = parse_input(&fs::read_to_string(filename).expect("File cannot be read"));

    println!("Part 1: {}", part_1(&instructions));
    println!("Part 2: {}", part_2(&instructions));
}
