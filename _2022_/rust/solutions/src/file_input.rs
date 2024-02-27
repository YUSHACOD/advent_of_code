pub fn get_input_lines(path: String) -> Option<Vec<String>> {
    let input = std::fs::read_to_string(path);

    //This spliting changes based on the quetion. I didn't bother mentioning them
    let result: Option<Vec<String>> = match input {
        Ok(value) => Some(value.split("\n\n").map(|x| String::from(x)).collect()),
        Err(_) => None,
    };

    match result {
        Some(result) => {
            //result.pop();
            Some(result)
        }
        None => None,
    }
}
