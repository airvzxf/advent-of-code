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

    best_ways = []
    MULTIPLICATION_BEST_WAYS = 1
    for index, record_time in enumerate(times):
        record_distance = distances[index]
        print(f'record_time: {record_time}')
        print(f'record_distance: {record_distance}')
        print()
        NUMBER_OF_WAYS = 0
        for time_hold_button in range(1, record_time + 1):
            print(f'time_hold_button: {time_hold_button}')
            travel_time = record_time - time_hold_button
            print(f'travel_time: {travel_time}')
            distance_traveled = time_hold_button * travel_time
            print(f'distance_traveled: {distance_traveled}')
            if distance_traveled > record_distance:
                NUMBER_OF_WAYS += 1
            print()
        best_ways.append(NUMBER_OF_WAYS)
        MULTIPLICATION_BEST_WAYS *= NUMBER_OF_WAYS
        print(f'best_ways: {best_ways}')
        print()
        print()

    print(f'MULTIPLICATION_BEST_WAYS: {MULTIPLICATION_BEST_WAYS}')
