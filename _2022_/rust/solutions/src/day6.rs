use std::collections::HashMap;
use std::collections::VecDeque;

fn has_all_unique_elements(window: &VecDeque<char>) -> bool {
    let mut map: HashMap<char, u8> = HashMap::new();
    for x in window.iter() {
        match map.get(x) {
            Some(v) => map.insert(x.clone(), v + 1),
            None => map.insert(x.clone(), 1),
        };
    }
    map.len() == window.len()
}

fn get_starter_marker(s: &String) -> u32 {
    let mut window: VecDeque<char> = VecDeque::new();
    let mut marker: u32 = 0;
    for c in s.chars() {
        marker += 1;
        if window.len() != 14 {
            window.push_back(c);
        } else {
            window.pop_front();
            window.push_back(c);
            if has_all_unique_elements(&window) {
                break;
            }
        }
    }
    marker
}

pub fn solution(input: &Vec<String>) -> u32 {
    let mut result: u32 = 0;
    for s in input {
        result += get_starter_marker(s);
    }
    result
}
