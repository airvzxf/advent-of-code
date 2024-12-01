use std::fs::read_to_string;

/// Reads a file containing space-separated integers and returns a vector of these integers.
///
/// # Arguments
///
/// * `input_path` - A string slice representing the path to the input file.
///
/// # Returns
///
/// * A `Vec<i32>` containing the integers read from the input file.
///
/// # Errors
///
/// If the file cannot be read, this function will panic with a message indicating the failure.
fn extract_numbers(input_path: &str) -> Vec<i32> {
    let input: String = read_to_string(input_path).expect("Failed to read input");

    input
        .split_whitespace()
        .map(|n| n.parse().unwrap())
        .collect()
}

/// Extracts and returns a vector of integers from the input vector,
/// containing only the elements at even indices.
///
/// # Parameters
///
/// * `numbers` - A reference to a slice of `i32` representing the input vector.
///
/// # Returns
///
/// * A `Vec<i32>` containing the integers at even indices from the input vector.
fn extract_left_list(numbers: &[i32]) -> Vec<i32> {
    numbers
        .iter()
        .enumerate()
        .step_by(2)
        .map(|(_, &n)| n)
        .collect()
}

/// Extracts and returns a vector of integers from the input vector,
/// containing only the elements at odd indices.
///
/// # Parameters
///
/// * `numbers` - A reference to a slice of `i32` representing the input vector.
///
/// # Returns
///
/// * A `Vec<i32>` containing the integers at odd indices from the input vector.
fn extract_right_list(numbers: &[i32]) -> Vec<i32> {
    numbers
        .iter()
        .enumerate()
        .filter(|&(index, _)| index % 2 != 0)
        .map(|(_, &n)| n)
        .collect()
}

/// Solves part 1 of the problem.
///
/// This function reads a list of integers from the input file,
/// sorts the even-indexed numbers in ascending order,
/// sorts the odd-indexed numbers in ascending order,
/// and calculates the sum of absolute differences between corresponding elements in the two sorted lists.
///
/// # Arguments
///
/// * `input_path` - A string slice representing the path to the input file.
/// * `debug` - A boolean indicating whether debug information should be printed.
///
/// # Returns
///
/// * An `i32` representing the sum of absolute differences between corresponding elements in the two sorted lists.
pub fn solve_part_1(input_path: &str, debug: bool) -> i32 {
    let numbers: Vec<i32> = extract_numbers(input_path);
    let left_list: Vec<i32> = extract_left_list(&numbers);
    let right_list: Vec<i32> = extract_right_list(&numbers);

    let mut left_list_sorted: Vec<i32> = left_list.clone();
    let mut right_list_sorted: Vec<i32> = right_list.clone();
    left_list_sorted.sort_unstable();
    right_list_sorted.sort_unstable();

    let mut distance: i32 = 0;
    for i in 0..left_list_sorted.len() {
        distance += (left_list_sorted[i] - right_list_sorted[i]).abs();
        if debug {
            println!(
                "{} {} = {} | {}",
                left_list_sorted[i],
                right_list_sorted[i],
                (left_list_sorted[i] - right_list_sorted[i]).abs(),
                distance
            );
        }
    }

    distance
}

/// Solves part 2 of the problem.
///
/// This function reads a list of integers from the input file,
/// calculates the product of each number in the even-indexed list with the count of its occurrences in the odd-indexed list,
/// and accumulates the results to find the total similarity score.
///
/// # Arguments
///
/// * `input_path` - A string slice representing the path to the input file.
/// * `debug` - A boolean indicating whether debug information should be printed.
///
/// # Returns
///
/// * An `i32` representing the total similarity score calculated by multiplying each number in the even-indexed list
///   with the count of its occurrences in the odd-indexed list and accumulating the results.
pub fn solve_part_2(input_path: &str, debug: bool) -> i32 {
    let numbers: Vec<i32> = extract_numbers(input_path);
    let left_list: Vec<i32> = extract_left_list(&numbers);
    let right_list: Vec<i32> = extract_right_list(&numbers);

    let mut similarity: i32 = 0;
    for &left_number in &left_list {
        let repetition: i32 = right_list.iter().filter(|&&n| n == left_number).count() as i32;
        similarity += left_number * repetition;
        if debug {
            println!(
                "{} x {} = {} | {}",
                left_number,
                repetition,
                left_number * repetition as i32,
                similarity
            );
        }
    }

    similarity
}
