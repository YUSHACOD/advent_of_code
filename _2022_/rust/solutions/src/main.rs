mod day11;
mod input;

fn main() {
    let argument: Vec<String> = std::env::args().collect();
    let input = input::get_input_lines(argument[1].to_string());
    match input {
        Some(in_string) => {
            let solution = day11::solution(&in_string);
            println!("Solution : {solution}");
        }
        None => println!("Error"),
    }
}
