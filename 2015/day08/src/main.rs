use std::ops::Add;
use std::{env, fs};

fn get_memory_chars(string: &str) -> String {
    let mut in_escape_sequence = false;
    let mut escape_sequence = String::new();
    let mut parsed_string = String::new();
    for (pos, chr) in string.chars().enumerate() {
        if pos == 0 || pos == string.len() - 1 {
            continue;
        }

        if !in_escape_sequence {
            if chr == '\\' {
                in_escape_sequence = true;
            } else {
                parsed_string.push(chr)
            }
        } else {
            let joined_seq = [&escape_sequence, chr.to_string().as_str()].join("");
            if !joined_seq.starts_with("x") {
                parsed_string.push(chr);
                in_escape_sequence = false;
                escape_sequence.clear();
            } else {
                escape_sequence.push(chr);
                if joined_seq.len() == 3 {
                    in_escape_sequence = false;
                    escape_sequence.clear();
                    parsed_string.push('x');
                }
            }
        }
    }
    return parsed_string;
}

fn encode_str(string: &str) -> String {
    let mut encoded_string = String::from("\"");
    for chr in string.chars() {
        if ['\\', '"'].contains(&chr) {
            encoded_string.push('\\');
            encoded_string.push(chr);
        } else {
            encoded_string.push(chr);
        }
    }
    encoded_string.push('"');
    return encoded_string;
}

fn main() {
    let args: Vec<String> = env::args().collect();
    let filename = &args[1];
    let string = fs::read_to_string(filename).expect("File cannot be read");
    let mut total_string_chars = 0;
    let mut total_mem_chars = 0;
    let mut encoded_mem_chars = 0;
    for line in string.lines() {
        total_string_chars += line.len();
        total_mem_chars += get_memory_chars(line).len();
        encoded_mem_chars += encode_str(line).len();
    }

    println!("Part 1: {}", total_string_chars - total_mem_chars);
    println!("Part 2: {}", encoded_mem_chars - total_string_chars);
}
