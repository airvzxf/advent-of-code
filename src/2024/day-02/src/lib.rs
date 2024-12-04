use std::fs::read_to_string;

pub fn solve_part_1(input: &str, debug: bool) -> i32 {
    let file_content: String = read_to_string(input).expect("Failed to read input file");

    let lines: Vec<Vec<i32>> = file_content
        .lines()
        .map(|line| {
            line.split_whitespace()
                .map(|num_str| {
                    num_str
                        .parse::<i32>()
                        .expect("Failed to parse input number")
                })
                .collect()
        })
        .collect();

    let mut total_safe: i32 = 0;
    for row in &lines {
        let equal: bool = row[0] == row[1];
        if equal {
            if debug {
                println!("Row: {:?} | Unsafe | Equal numbers", row);
            }
            continue;
        }

        let increasing: bool = row[0] < row[1];
        let decreasing: bool = row[0] > row[1];

        let mut is_safe: bool = true;
        for i in 1..row.len() {
            let distance = row[i].abs_diff(row[i - 1]);
            if distance > 3 {
                if debug {
                    println!("Row: {:?} | Unsafe | Distance: {}", row, distance);
                }
                is_safe = false;
                break;
            }

            if increasing && row[i] <= row[i - 1] {
                if debug {
                    println!("Row: {:?} | Unsafe | It is not increasing", row);
                }
                is_safe = false;
                break;
            } else if decreasing && row[i] >= row[i - 1] {
                if debug {
                    println!("Row: {:?} | Unsafe | It is not decreasing", row);
                }
                is_safe = false;
                break;
            } else if row[i] == row[i - 1] {
                if debug {
                    println!("Row: {:?} | Unsafe | It is equal", row);
                }
                is_safe = false;
                break;
            }
        }

        if is_safe {
            if debug {
                println!("Row: {:?} | Safe", row);
            }
            total_safe += 1;
        };
    }

    total_safe
}

fn validate_row(row: &Vec<i32>, debug: bool) -> bool {
    let row_size: usize = row.len() - 1;
    let mut count_increasing: usize = 0;
    let mut count_decreasing: usize = 0;

    for i in 1..row.len() {
        let distance: i32 = row[i - 1] - row[i];
        let abs_distance: i32 = distance.abs();

        if abs_distance > 3 {
            if debug {
                println!("Row: {:?} | Unsafe | Distance: {}", row, abs_distance);
            }
            return false;
        }

        match distance {
            x if x < 0 => count_increasing += 1,
            x if x > 0 => count_decreasing += 1,
            _ => {}
        }
    }

    if debug {
        println!("Row: {:?}", row);
        println!(
            "Size: {} | Increasing: {} | Decreasing: {}",
            row_size, count_increasing, count_decreasing
        );
    }

    if row_size == count_increasing || row_size == count_decreasing {
        return true;
    }

    false
}

pub fn solve_part_2(input: &str, debug: bool) -> i32 {
    let file_content: String = read_to_string(input).expect("Failed to read input file");

    let lines: Vec<Vec<i32>> = file_content
        .lines()
        .map(|line| {
            line.split_whitespace()
                .map(|num_str| {
                    num_str
                        .parse::<i32>()
                        .expect("Failed to parse input number")
                })
                .collect()
        })
        .collect();

    let mut total_safe: i32 = 0;
    'lines_by_row: for row in &lines {
        if debug {
            println!();
        }
        let valid_row: bool = validate_row(row, debug);
        if valid_row {
            if debug {
                println!("### VALID ###");
            }
            total_safe += 1;
            continue;
        } else if debug {
            println!("~~~ INVALID ~~~");
        }

        for i in 0..row.len() {
            let mut new_row: Vec<i32> = row.clone();
            new_row.remove(i);
            let valid_row: bool = validate_row(&new_row, debug);
            if valid_row {
                if debug {
                    println!("# VALID #");
                }
                total_safe += 1;
                continue 'lines_by_row;
            } else if debug {
                println!("~ INVALID ~");
            }
        }
    }

    total_safe
}
