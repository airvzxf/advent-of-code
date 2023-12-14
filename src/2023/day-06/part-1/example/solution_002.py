#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
Solution of the AoC 2023, day 6.
"""

if __name__ == '__main__':
    times = (
        (7, 15, 30)
    )

    distances = (
        (9, 40, 200)
    )

    solution = (
        (4, 8, 9)
    )

    SOLUTION_MULTIPLICATION = 288

    MULTIPLICATION_BEST_WAYS = 1
    for index, record_time in enumerate(times):
        record_distance = distances[index]
        print(f'record_time: {record_time}')
        print(f'record_distance: {record_distance}')
        print()
        NUMBER_OF_BAD_WAYS = 0
        for time_hold_button in range(0, record_time + 1):
            print(f'time_hold_button: {time_hold_button}')
            travel_time = record_time - time_hold_button
            print(f'travel_time: {travel_time}')
            distance_traveled = time_hold_button * travel_time
            print(f'distance_traveled: {distance_traveled}')
            if distance_traveled > record_distance:
                break
            NUMBER_OF_BAD_WAYS += 1
            print(f'NUMBER_OF_BAD_WAYS: {NUMBER_OF_BAD_WAYS}')
            print()
        print(f'NUMBER_OF_BAD_WAYS * 2 - 1: {NUMBER_OF_BAD_WAYS * 2 - 1}')
        correct_ways = record_time - (NUMBER_OF_BAD_WAYS * 2 - 1)
        print(f'correct_ways: {correct_ways}')
        assert correct_ways == solution[index]
        MULTIPLICATION_BEST_WAYS *= correct_ways
        print()
        print()

    print(f'MULTIPLICATION_BEST_WAYS: {MULTIPLICATION_BEST_WAYS}')
    assert MULTIPLICATION_BEST_WAYS == SOLUTION_MULTIPLICATION
