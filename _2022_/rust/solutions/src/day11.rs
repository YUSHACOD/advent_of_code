#[allow(dead_code)]
#[derive(Debug)]
enum Operation {
    Add(usize),
    Multiply(usize),
    Square,
}

#[allow(dead_code)]
#[derive(Debug)]
struct Monkey {
    items: Vec<usize>,
    operation: Operation,
    filter: usize,
    if_true: usize,
    if_false: usize,
    inspections: usize,
}

fn create_monkey(monkey_data: &String) -> Monkey {
    let lines: Vec<String> = monkey_data
        .trim()
        .split("\n")
        .map(|x| x.trim().to_string())
        .collect();

    let items_t: Vec<usize> = lines[1]
        .replace("Starting items:", "")
        .trim()
        .split(", ")
        .map(|x| x.parse().unwrap_or(0))
        .collect();

    let operation_t: Operation = {
        let symbols: Vec<String> = lines[2]
            .replace("Operation: new =", "")
            .trim()
            .split_whitespace()
            .map(|x| x.to_string())
            .collect();

        match (&symbols[0][..], &symbols[1][..], &symbols[2][..]) {
            (_, "*", "old") => Operation::Square,
            (_, "*", operand) => Operation::Multiply(operand.parse().unwrap_or(1)),
            (_, "+", operand) => Operation::Add(operand.parse().unwrap_or(1)),
            _ => Operation::Add(0),
        }
    };

    Monkey {
        items: items_t,
        operation: operation_t,
        filter: lines[3]
            .trim()
            .replace("Test: divisible by", "")
            .trim()
            .parse()
            .unwrap_or(1),
        if_true: lines[4]
            .trim()
            .replace("If true: throw to monkey", "")
            .trim()
            .parse()
            .unwrap_or(1),
        if_false: lines[5]
            .trim()
            .replace("If true: throw to monkey", "")
            .trim()
            .parse()
            .unwrap_or(1),
        inspections: 0,
    }
}

pub fn solution(input: &Vec<String>) -> usize {
    let monkeys: Vec<Monkey> = input
        .iter()
        .map(|monkey_data| create_monkey(monkey_data))
        .collect();

    dbg!(&input);
    dbg!(&monkeys);

    0
}
