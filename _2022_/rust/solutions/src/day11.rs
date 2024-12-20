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

impl Monkey {
    fn operate(&self, value: &usize, group_limit: usize) -> usize {
        let worry_value = match self.operation {
            Operation::Add(operand) => value + operand,

            Operation::Multiply(operand) => {
                dbg!(value);
                value * operand
            }

            Operation::Square => value * value,
        };
        worry_value % group_limit
    }

    fn inspect_all_items(&mut self, group_limit: usize) -> (Vec<usize>, Vec<usize>) {
        let mut true_throws: Vec<usize> = Vec::new();
        let mut false_throws: Vec<usize> = Vec::new();
        self.items.iter().fold(0, |acc, x| {
            let worry_value = self.operate(x, group_limit);

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

    let items_t: Vec<usize> = lines[1]
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

pub fn solution(input: &Vec<String>) -> usize {
    let mut group_limit: usize = 1;
    let mut monkeys: Vec<Monkey> = input
        .iter()
        .map(|x| {
            let x = create_monkey(x);
            group_limit *= x.filter;
            x
        })
        .collect();

    for _round in 0..10000 {
        for i in 0..monkeys.len() {
            let (mut true_throws, mut false_throws) = monkeys[i].inspect_all_items(group_limit);
            let true_idx = monkeys[i].if_true;
            let false_idx = monkeys[i].if_false;
            monkeys[i].inspections += true_throws.len() + false_throws.len();
            monkeys[true_idx].items.append(&mut true_throws);
            monkeys[false_idx].items.append(&mut false_throws);
        }
    }

    let mut simian_activity: Vec<usize> = Vec::new();
    for i in 0..monkeys.len() {
        simian_activity.push(monkeys[i].inspections);
    }

    simian_activity.sort();
    simian_activity.reverse();
    simian_activity[0] * simian_activity[1]
}
