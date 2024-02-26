use std::usize;

fn is_visible(position: (usize, usize), forest: &Vec<Vec<usize>>) -> bool {
    let (y, x) = position;
    let length = forest.len();

    //for right
    let mut v_from_right = true;
    for r_idx in (x + 1)..length {
        if forest[y][r_idx] >= forest[y][x] {
            v_from_right = false;
            break;
        }
    }

    //for down
    let mut v_from_down = true;
    for d_idx in (y + 1)..length {
        if forest[d_idx][x] >= forest[y][x] {
            v_from_down = false;
            break;
        }
    }

    //for left
    let mut v_from_left = true;
    for l_idx in (0..x).rev() {
        if forest[y][l_idx] >= forest[y][x] {
            v_from_left = false;
            break;
        }
    }

    //for up
    let mut v_from_up = true;
    for u_idx in (0..y).rev() {
        if forest[u_idx][x] >= forest[y][x] {
            v_from_up = false;
            break;
        }
    }

    v_from_right || v_from_down || v_from_left || v_from_up
}

fn count_visible_trees(forest: &Vec<Vec<usize>>) -> usize {
    let length = forest.len();
    let mut count: usize = length * 4 - 4;
    for y in 1..length - 1 {
        for x in 1..length - 1 {
            if is_visible((y, x), &forest) {
                count += 1;
            }
        }
    }
    count
}

fn get_scenic_value(position: (usize, usize), forest: &Vec<Vec<usize>>) -> usize {
    let (y, x) = position;
    let length = forest.len();

    //for right
    let mut v_from_right: usize = 0;
    for r_idx in (x + 1)..length {
        if forest[y][r_idx] >= forest[y][x] {
            v_from_right += 1;
            break;
        }
        v_from_right += 1;
    }

    //for down
    let mut v_from_down: usize = 0;
    for d_idx in (y + 1)..length {
        if forest[d_idx][x] >= forest[y][x] {
            v_from_down += 1;
            break;
        }
        v_from_down += 1;
    }

    //for left
    let mut v_from_left: usize = 0;
    for l_idx in (0..x).rev() {
        if forest[y][l_idx] >= forest[y][x] {
            v_from_left += 1;
            break;
        }
        v_from_left += 1;
    }

    //for up
    let mut v_from_up: usize = 0;
    for u_idx in (0..y).rev() {
        if forest[u_idx][x] >= forest[y][x] {
            v_from_up += 1;
            break;
        }
        v_from_up += 1;
    }

    v_from_right * v_from_down * v_from_left * v_from_up
}

fn get_most_scenic_value(forest: &Vec<Vec<usize>>) -> usize {
    let length = forest.len();
    let mut scenic_value: usize = 0;
    for y in 1..length - 1 {
        for x in 1..length - 1 {
            let value = get_scenic_value((y, x), &forest);
            if value > scenic_value {
                scenic_value = value;
            }
        }
    }
    scenic_value
}

pub fn solution(input: &Vec<String>) -> usize {
    let mut forest: Vec<Vec<usize>> = Vec::new();

    for line in input {
        forest.push(
            line.chars()
                .map(|x| x.to_digit(10).unwrap_or(0) as usize)
                .collect(),
        )
    }

    let solution1 = count_visible_trees(&forest);
    dbg!(solution1);

    get_most_scenic_value(&forest)
}
