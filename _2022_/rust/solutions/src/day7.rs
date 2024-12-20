use std::{collections::HashMap, usize};

fn create_total_path(stack: &Vec<String>) -> String {
    let mut s = String::new();
    for file in stack {
        s = s + file + "/";
    }
    s
}

fn create_total_paths(mut stack: Vec<String>) -> Vec<String> {
    let mut result: Vec<String> = Vec::new();
    for _ in 0..stack.len() {
        result.push(create_total_path(&stack));
        stack.pop();
    }
    result
}

fn apply_instructions(instructions: &Vec<String>) -> HashMap<String, usize> {
    let mut result: HashMap<String, usize> = HashMap::new();
    let mut stack: Vec<String> = Vec::new();

    for instruction in instructions {
        let instruction: Vec<String> = instruction
            .split_whitespace()
            .map(|x| String::from(x))
            .collect();

        if instruction.len() == 0 {
            break;
        }

        //dbg!(&instruction);
        //dbg!(&stack);

        match &instruction[0][..] {
            "$" => {
                match &instruction[1][..] {
                    "cd" => {
                        match &instruction[2][..] {
                            ".." => {
                                stack.pop();
                            }
                            _ => {
                                stack.push(instruction[2].clone());
                                dbg!(create_total_path(&stack));
                                result.insert(create_total_path(&stack), 0);
                            }
                        };
                    }
                    "ls" => (),
                    _ => {
                        println!("In command shit happened!");
                        dbg!(&instruction);
                    }
                };
            }
            "dir" => (),
            _ => {
                let f_size = instruction[0].trim().parse().unwrap_or(0);
                let folders: Vec<String> = create_total_paths(stack.clone());
                dbg!(&folders);
                for folder in folders {
                    match result.get(&folder) {
                        Some(size) => {
                            match result.insert(folder.clone(), size + f_size) {
                                Some(_) => (),
                                None => println!("somethings wrong"),
                            };
                        }
                        None => println!("Somethings wrong check the hashmap!"),
                    };
                }
            }
        };
    }

    result
}

pub fn solution(input: &Vec<String>) -> usize {
    let dir_sizes = apply_instructions(input);
    let size_limit: usize = 100000;
    dbg!(&dir_sizes);
    let solution1 = dir_sizes.clone().values().into_iter().fold(0, |acc, x| {
        //dbg!(x);
        if x <= &size_limit {
            //dbg!(acc + x);
            acc + x
        } else {
            //dbg!(acc);
            acc
        }
    });
    dbg!(solution1);

    let root_size: usize = match dir_sizes.get("//") {
        Some(value) => value.to_owned(),
        None => 0,
    };
    dbg!(root_size);
    let mut space_required: usize = 0;
    if root_size > 40000000 {
        space_required = root_size - 40000000;
    }
    dbg!(space_required);
    let mut list: Vec<usize> = Vec::new();
    for y in dir_sizes.values() {
        if y >= &space_required {
            list.push(y.to_owned());
        }
    }
    dbg!(&list);
    let solution2 = list
        .iter()
        .fold(&list[0], |acc, x| if x < acc { &x } else { &acc });
    solution2.to_owned()
}
