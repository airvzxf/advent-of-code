use aoc_2021_day_02::{solve_part_1, solve_part_2};

fn main() {
    let input = "resources/input-01-puzzle.txt";
    let debug = false;
    let safe = solve_part_1(input, debug);
    println!("Part 1 | {} safe reports\n\n\n", safe);

    let input = "resources/input-02-puzzle.txt";
    let debug = false;
    let safe = solve_part_2(input, debug);
    println!("Part 2 | {} safe reports", safe);
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_part_1_example() {
        let input = "resources/input-01-example.txt";
        let debug = false;
        let safe = solve_part_1(input, debug);
        assert_eq!(safe, 2);
    }

    #[test]
    fn test_part_1_puzzle() {
        let input = "resources/input-01-puzzle.txt";
        let debug = false;
        let safe = solve_part_1(input, debug);
        assert_eq!(safe, 660);
    }

    #[test]
    fn test_part_2_example() {
        let input = "resources/input-02-example.txt";
        let debug = false;
        let safe = solve_part_2(input, debug);
        assert_eq!(safe, 4);
    }

    #[test]
    fn test_part_2_puzzle() {
        let input = "resources/input-02-puzzle.txt";
        let debug = false;
        let safe = solve_part_2(input, debug);
        assert_eq!(safe, 689);
    }
}
