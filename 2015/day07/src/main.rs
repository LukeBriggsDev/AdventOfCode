use std::collections::HashMap;
use std::{env, fs};

fn parse_input(input_string: &str) -> Vec<(Vec<&str>, &str)> {
    let mut instructions = Vec::new();

    for line in input_string.lines() {
        let mut split_instruction = line.split(" -> ");
        let input = split_instruction
            .next()
            .unwrap()
            .split(" ")
            .collect::<Vec<&str>>();
        let output = split_instruction.next().unwrap();
        instructions.push((input, output))
    }

    return instructions;
}

fn value_of(value: &str, variables: &HashMap<&str, u16>) -> u16 {
    if value.parse::<u16>().is_ok() {
        return value.parse::<u16>().unwrap();
    } else {
        return match variables.get(value) {
            Some(value) => value.clone(),
            _ => panic!("{}", value),
        };
    }
}

fn run_instruction(variables: &HashMap<&str, u16>, instruction: &Vec<&str>) -> u16 {
    let mut operation = "ASSIGNMENT";

    for value in instruction {
        if ["AND", "OR", "LSHIFT", "RSHIFT", "NOT"].contains(&value) {
            operation = value
        }
    }
    return match operation {
        "AND" => value_of(instruction[0], &variables) & value_of(instruction[2], &variables),
        "OR" => value_of(instruction[0], &variables) | value_of(instruction[2], &variables),
        "LSHIFT" => value_of(instruction[0], &variables) << value_of(instruction[2], &variables),
        "RSHIFT" => value_of(instruction[0], &variables) >> value_of(instruction[2], &variables),
        "NOT" => !value_of(instruction[1], &variables),
        "ASSIGNMENT" => value_of(instruction[0], &variables),
        _ => panic!("NOT AN OPERATION"),
    };
}

fn run_program<'a, 'b>(instructions: &Vec<(Vec<&'a str>, &'b str)>) -> HashMap<&'b str, u16> {
    let mut variables = HashMap::new();

    let operations = ["AND", "OR", "LSHIFT", "RSHIFT", "NOT"];

    let mut any_unknowns = true;
    while any_unknowns {
        any_unknowns = false;
        for (input, output) in instructions.clone() {
            let mut unknowns = false;
            for value in &input {
                if !variables.contains_key(value)
                    && !operations.contains(&value)
                    && value.parse::<u16>().is_err()
                {
                    unknowns = true;
                    any_unknowns = true;
                    break;
                }
            }
            if !unknowns {
                variables.insert(output, run_instruction(&variables, &input));
            }
        }
    }
    return variables;
}

fn main() {
    let args: Vec<String> = env::args().collect();
    let filename = &args[1];
    let string = fs::read_to_string(filename).expect("File cannot be read");
    let instructions = parse_input(&string);
    let variables = run_program(&instructions);

    let part_1_answer = variables.get("a").unwrap();
    let part_1_answer: &str = &part_1_answer.to_string();
    println!("PART 1: {}", part_1_answer);

    // Part 2
    let mut new_instructions = Vec::new();
    for (input, output) in instructions.iter() {
        if input.len() == 1 && input[0].parse::<u16>().is_ok() && output == &"b" {
            new_instructions.push(([part_1_answer].to_vec(), "b"));
        } else {
            new_instructions.push((input.clone(), output))
        }
    }
    let variables = run_program(&new_instructions);
    let part_2_answer = variables.get("a").unwrap();
    println!("PART 2: {}", part_2_answer);
}
