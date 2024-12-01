#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
Solution of the AoC 2023. Day 9, part 1 and it is the solution of the example.
"""


def all_zeros(record: tuple) -> int:
    last_digit = []
    current_record = list(record)

    while sum(current_record) != 0:
        last_digit.append(current_record[-1])
        print(f'Last digit: {last_digit}')
        new_record = []
        len_current_record = len(current_record)
        for index in range(len_current_record - 1):
            difference = current_record[index + 1] - current_record[index]
            print(f'Current digit: {current_record[index + 1]} - {current_record[index]} = {difference}')
            new_record.append(difference)

        print(f'New record: {new_record}')
        current_record = new_record
        print()

    print(f'last_digit: {last_digit}')
    print()
    return sum(last_digit)


if __name__ == "__main__":
    history = (
        (0, 3, 6, 9, 12, 15),
        (1, 3, 6, 10, 15, 21),
        (10, 13, 16, 21, 30, 45),
    )

    discovered_numbers = []
    for record in history:
        number = all_zeros(record)
        discovered_numbers.append(number)

    print(f'Discovered numbers: {discovered_numbers}')
    print(f'Sum of all numbers: {sum(discovered_numbers)}')
