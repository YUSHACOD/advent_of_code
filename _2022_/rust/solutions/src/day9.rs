#[derive(Debug)]
struct Rope {
    head: (isize, isize),
    tail: (isize, isize),
    visits: Vec<(isize, isize)>,
}

fn maintain_rope_length(rope: &mut Rope) {
    if rope.head != rope.tail {
        let x_diff = rope.head.0 - rope.tail.0;
        let y_diff = rope.head.1 - rope.tail.1;

        if (x_diff.abs() == 2) || (y_diff.abs() == 2) {
            if (x_diff.abs() >= 1) && (y_diff.abs() >= 1) {
                if (x_diff.abs() == 2) && (y_diff.abs() == 1) {
                    rope.tail.0 += if x_diff < 0 { x_diff + 1 } else { x_diff - 1 };
                    rope.tail.1 += y_diff;
                } else if (x_diff.abs() == 1) && (y_diff.abs() == 2) {
                    rope.tail.0 += x_diff;
                    rope.tail.1 += if y_diff < 0 { y_diff + 1 } else { y_diff - 1 };
                } else if (x_diff.abs() == 2) && (y_diff.abs() == 2) {
                    rope.tail.0 += if x_diff < 0 { x_diff + 1 } else { x_diff - 1 };
                    rope.tail.1 += if y_diff < 0 { y_diff + 1 } else { y_diff - 1 };
                } else {
                    println!("Somethings terribly wrong!");
                    dbg!(&rope.head);
                    dbg!(&rope.tail);
                }
            } else if (x_diff.abs() == 2) && (y_diff.abs() == 0) {
                rope.tail.0 += if x_diff < 0 { x_diff + 1 } else { x_diff - 1 };
            } else if (x_diff.abs() == 0) && (y_diff.abs() == 2) {
                rope.tail.1 += if y_diff < 0 { y_diff + 1 } else { y_diff - 1 };
            } else {
                println!("Somethings wrong while maintaining the length!");
                dbg!(&rope.head);
                dbg!(&rope.tail);
            }

            if !rope.visits.contains(&rope.tail) {
                rope.visits.push(rope.tail);
            }
        }
    }
}

fn apply_instruction(rope: &mut Vec<Rope>, instruction: &(String, isize)) {
    match &instruction.0[..] {
        "R" => {
            for _ in 0..instruction.1 {
                rope[0].head.0 += 1;
                if rope.len() == 1 {
                    maintain_rope_length(&mut rope[0]);
                } else {
                    let len = rope.len();
                    for x in 0..len - 1 {
                        maintain_rope_length(&mut rope[x]);
                        rope[x + 1].head = rope[x].tail;
                    }
                    maintain_rope_length(&mut rope[len - 1]);
                }
            }
        }
        "L" => {
            for _ in 0..instruction.1 {
                rope[0].head.0 -= 1;
                if rope.len() == 1 {
                    maintain_rope_length(&mut rope[0]);
                } else {
                    let len = rope.len();
                    for x in 0..len - 1 {
                        maintain_rope_length(&mut rope[x]);
                        rope[x + 1].head = rope[x].tail;
                    }
                    maintain_rope_length(&mut rope[len - 1]);
                }
            }
        }
        "U" => {
            for _ in 0..instruction.1 {
                rope[0].head.1 += 1;
                if rope.len() == 1 {
                    maintain_rope_length(&mut rope[0]);
                } else {
                    let len = rope.len();
                    for x in 0..len - 1 {
                        maintain_rope_length(&mut rope[x]);
                        rope[x + 1].head = rope[x].tail;
                    }
                    maintain_rope_length(&mut rope[len - 1]);
                }
            }
        }
        "D" => {
            for _ in 0..instruction.1 {
                rope[0].head.1 -= 1;
                if rope.len() == 1 {
                    maintain_rope_length(&mut rope[0]);
                } else {
                    let len = rope.len();
                    for x in 0..len - 1 {
                        maintain_rope_length(&mut rope[x]);
                        rope[x + 1].head = rope[x].tail;
                    }
                    maintain_rope_length(&mut rope[len - 1]);
                }
            }
        }
        _ => {
            println!("Some thing bad happened!");
            dbg!(&instruction);
        }
    };
}

fn get_tail_visits(instructions: Vec<(String, isize)>) -> usize {
    let mut rope: Vec<Rope> = Vec::new();
    let rope_length: usize = 9;
    for _ in 0..rope_length {
        rope.push(Rope {
            head: (0, 0),
            tail: (0, 0),
            visits: {
                let mut x = Vec::new();
                x.push((0, 0));
                x
            },
        });
    }

    for instruction in instructions {
        apply_instruction(&mut rope, &instruction);
    }

    rope[rope_length - 1].visits.len()
}

pub fn solution(input: &Vec<String>) -> usize {
    let mut instructions: Vec<(String, isize)> = Vec::new();
    for line in input {
        instructions.push({
            let x: Vec<String> = line
                .split_whitespace()
                .map(|x| String::from(x.trim()))
                .collect();
            (x[0].clone(), x[1].parse().unwrap_or(0))
        });
    }
    //dbg!(&input);
    //dbg!(&instructions);

    let solution1 = get_tail_visits(instructions);
    solution1
}
