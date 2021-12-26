use std::{env, fs};

struct Box {
    width: u32,
    length: u32,
    height: u32
}

impl Box {
    fn new(width:u32, length:u32, height:u32) -> Box {
        return Box {
            width,
            length,
            height
        }
    }
    fn required_paper(&self) -> u32 {
        let areas = [self.length * self.width, self.length * self.height, self.width * self.height];
        return 2 * areas.iter().sum::<u32>() + areas.iter().min().unwrap()

    }

    fn required_ribbon(&self) -> u32 {
        let mut sides = [self.length, self.width, self.height].to_vec();
        sides.sort();
        return 2*sides.get(0).unwrap() + 2*sides.get(1).unwrap() + self.length * self.height * self.width;

    }
}

fn main() {
    let args: Vec<String> = env::args().collect();
    let filename = &args.get(1).expect("problem input not passed");
    let boxes = fs::read_to_string(filename)
        .expect("File cannot be read");
    let boxes = boxes.split("\n");
    let mut box_list:Vec<Box> = Vec::new();

    for bx in boxes {
         box_list.push(
             match bx.split('x').collect::<Vec<&str>>()[0..3] {
                [width, length, height] => Box::new(width.parse().unwrap(),
                                                    length.parse().unwrap(),
                                                    height.parse().unwrap()),
                 _ => panic!("Invalid dimension given")
         })
    }

    let mut total_paper = 0;
    let mut total_ribbon = 0;

    for bx in box_list {
        total_paper += bx.required_paper();
        total_ribbon += bx.required_ribbon();
    }

    println!("Part 1: {}", total_paper);
    println!("Part 2: {}", total_ribbon);

}
