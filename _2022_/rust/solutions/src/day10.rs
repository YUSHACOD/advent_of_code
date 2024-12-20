#[derive(Debug)]
enum Instruction {
    Addx(isize),
    Noop,
}

fn crt_draw(cycle_counter: isize, register_x: isize) {
    let pixel_pos = cycle_counter % 40 - 1;
    if ((register_x - 1)..=(register_x + 1)).contains(&pixel_pos) {
        print!("#");
    } else {
        print!(" ");
    }

    if cycle_counter % 40 == 0 {
        println!();
    }
}

fn simulate_crt(instructions: Vec<Instruction>) -> isize {
    let mut cycle_counter: isize = 0;
    let mut strength_cycle: isize = 20;
    let mut register_x: isize = 1;
    let mut signal_strength_acc: isize = 0;

    for instruction in instructions {
        match instruction {
            Instruction::Addx(value) => {
                for i in 0..2 {
                    cycle_counter += 1;
                    crt_draw(cycle_counter, register_x);
                    if cycle_counter == strength_cycle {
                        signal_strength_acc += cycle_counter * register_x;
                        strength_cycle += 40;
                    }
                    if i == 1 {
                        register_x += value;
                    }
                }
            }
            Instruction::Noop => {
                cycle_counter += 1;
                crt_draw(cycle_counter, register_x);
                if cycle_counter == strength_cycle {
                    signal_strength_acc += cycle_counter * register_x;
                    strength_cycle += 40;
                }
            }
        };
    }

    signal_strength_acc
}

pub fn solution(input: &Vec<String>) -> isize {
    let instructions: Vec<Instruction> = input
        .iter()
        .map(|x| {
            let temp: Vec<String> = x.split_whitespace().map(|x| x.to_string()).collect();
            if temp.len() == 1 {
                Instruction::Noop
            } else {
                Instruction::Addx(temp[1].parse().unwrap_or(0))
            }
        })
        .collect();
    simulate_crt(instructions)
}
