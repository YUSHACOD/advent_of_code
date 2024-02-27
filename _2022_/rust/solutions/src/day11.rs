#[allow(dead_code)]
#[derive(Debug)]
enum Operation {
    Add(u128),
    Multiply(u128),
    Square,
}

#[allow(dead_code)]
#[derive(Debug)]
struct Monkey {
    items: Vec<u128>,
    operation: Operation,
    filter: u128,
    if_true: u128,
    if_false: u128,
    inspections: u128,
}

impl Monkey {
    fn operate(&self, value: &u128) -> u128 {
        match self.operation {
            Operation::Add(operand) => value + operand,

            Operation::Multiply(operand) => {
                dbg!(value);
                value * operand
            }

            Operation::Square => value * value,
        }
    }

    fn inspect_all_items(&mut self) -> (Vec<u128>, Vec<u128>) {
        let mut true_throws: Vec<u128> = Vec::new();
        let mut false_throws: Vec<u128> = Vec::new();
        self.items.iter().fold(0, |acc, x| {
            let worry_value = self.operate(x);

            if worry_value % self.filter == 0 {
                true_throws.push(worry_value);
            } else {
                false_throws.push(worry_value);
            }

            acc
        });

        self.items.drain(0..self.items.len());

        (true_throws, false_throws)
    }
}

fn create_monkey(monkey_data: &String) -> Monkey {
    let lines: Vec<String> = monkey_data
        .trim()
        .split('\n')
        .map(|x| x.trim().to_string())
        .collect();

    //dbg!(&lines);

    let items_t: Vec<u128> = lines[1]
        .replace("Starting items:", "")
        .trim()
        .split(", ")
        .map(|x| x.parse().unwrap_or(0))
        .collect();

    let operation_t: Operation = {
        let symbols: Vec<String> = lines[2]
            .replace("Operation: new =", "")
            .split_whitespace()
            .map(String::from)
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
            .replace("If false: throw to monkey", "")
            .trim()
            .parse()
            .unwrap_or(1),

        inspections: 0,
    }
}

pub fn solution(input: &Vec<String>) -> u128 {
    let mut monkeys: Vec<Monkey> = input.iter().map(create_monkey).collect();

    //dbg!(&input);
    //dbg!(&monkeys);

    for _round in 0..10000 {
        //println!("################################################");
        //println!("Round {}", round + 1);
        for i in 0..monkeys.len() {
            let (mut true_throws, mut false_throws) = monkeys[i].inspect_all_items();
            let true_idx = monkeys[i].if_true;
            let false_idx = monkeys[i].if_false;
            monkeys[i].inspections += true_throws.len() as u128 + false_throws.len() as u128;
            //dbg!((&true_throws, &false_throws));
            monkeys[true_idx as usize].items.append(&mut true_throws);
            monkeys[false_idx as usize].items.append(&mut false_throws);
        }
        /*
        for i in 0..monkeys.len() {
            dbg!((&monkeys[i].items, i));
            dbg!(&monkeys[i].inspections);
        }
        */
        //println!("Round {}", round + 1);
        //println!("################################################");
    }

    let mut simian_activity: Vec<u128> = Vec::new();
    for i in 0..monkeys.len() {
        dbg!((&monkeys[i].items, i));
        dbg!(&monkeys[i].inspections);
        simian_activity.push(monkeys[i].inspections);
    }

    simian_activity.sort(); 
    simian_activity.reverse(); 
    simian_activity[0] * simian_activity[1]
}
