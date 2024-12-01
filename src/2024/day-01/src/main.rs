use aoc_2021_day_01::{solve_part_1, solve_part_2};

fn main() {
    let input_path = "resources/input-01-puzzle.txt";
    let debug = false;
    let distance = solve_part_1(input_path, debug);
    println!("Part 1 | Total distance: {}", distance);

    let input_path = "resources/input-02-puzzle.txt";
    let debug = false;
    let similarity = solve_part_2(input_path, debug);
    println!("Part 2 | Total of similarity score: {}", similarity);
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_solve_part_1_with_example() {
        let input_path = "resources/input-01-example.txt";
        let debug = false;
        let distance = solve_part_1(input_path, debug);
        assert_eq!(distance, 11);
    }

    #[test]
    fn test_solve_part_1_with_puzzle() {
        let input_path = "resources/input-01-puzzle.txt";
        let debug = false;
        let distance = solve_part_1(input_path, debug);
        assert_eq!(distance, 1941353);
    }

    #[test]
    fn test_solve_part_2_with_example() {
        let input_path = "resources/input-02-example.txt";
        let debug = false;
        let similarity = solve_part_2(input_path, debug);
        assert_eq!(similarity, 31);
    }

    #[test]
    fn test_solve_part_2_with_puzzle() {
        let input_path = "resources/input-02-puzzle.txt";
        let debug = false;
        let similarity = solve_part_2(input_path, debug);
        assert_eq!(similarity, 22539317);
    }
}
