use std::{env, fs};
use fancy_regex::Regex;

fn is_nice_rule1(string: &str) ->  bool {
    let mut vowels = 0;
    let mut duplicate_letters = false;
    let characters = string.chars().collect::<Vec<char>>();
    for i in 0..characters.len() {
        if ['a', 'e', 'i', 'o', 'u'].contains(&characters.get(i).unwrap()) {
            vowels += 1;
        }
        if i < characters.len() - 1 {
            if characters[i] == characters[i + 1] {
                duplicate_letters = true
            }
            if ["ab", "cd", "pq", "xy"].contains(&format!("{}{}", characters[i], characters[i + 1]).as_str()) {
                return false;
            }
        }
    }

    return duplicate_letters && (vowels > 2)
}

fn is_nice_rule2(string: &str) ->  bool {
    let re_1 = Regex::new(r"(([a-zA-Z]{2}).*?\2)").unwrap();
    let re_2 = Regex::new(r"(([a-zA-Z])[a-zA-Z]\2)").unwrap();
    return re_1.is_match(string).unwrap() && re_2.is_match(string).unwrap();
}

fn main() {
    let args: Vec<String> = env::args().collect();
    let filename = &args[1];
    let strings = fs::read_to_string(filename).expect("File cannot be read");
    let strings = strings.split('\n');
    let mut nice_list1 = 0;
    let mut nice_list2 = 0;

    for string in strings {
        nice_list1 += if is_nice_rule1(string){ 1 } else { 0 };
        nice_list2 += if is_nice_rule2(string){ 1 } else { 0 };
    }

    println!("Part 1: {}", nice_list1);
    println!("Part 2: {}", nice_list2);
}
