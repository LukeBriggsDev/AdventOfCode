use std::{env, fs, fmt};
use md5;

fn get_lowest_zero_hash(first8: &str, no_of_zeroes: usize) -> u32{
    let mut last = 0;
    while !format!("{:x}", md5::compute(format!("{}{}", first8, last))).starts_with(&"0".repeat(no_of_zeroes)) {
        last += 1
    }
    return last;
}

fn main() {
    let args: Vec<String> = env::args().collect();
    let filename = &args[1];
    let first8 = fs::read_to_string(filename).expect("File cannot be read");


    println!("Part 1: {}", get_lowest_zero_hash(&first8, 5));
    println!("Part 2: {}", get_lowest_zero_hash(&first8, 6));

}
