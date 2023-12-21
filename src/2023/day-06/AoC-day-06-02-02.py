# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

if __name__ == '__main__':
    times = (
        56717999,
    )

    distances = (
        334113513502430,
    )

    best_ways = []
    multiplication_best_ways = 1
    for index, record_time in enumerate(times):
        record_distance = distances[index]
        print(f'record_time: {record_time}')
        print(f'record_distance: {record_distance}')
        # print()
        number_of_ways = 0
        for time_hold_button in range(1, record_time + 1):
            print(f'time_hold_button: {time_hold_button}')
            travel_time = record_time - time_hold_button
            # print(f'travel_time: {travel_time}')
            distance_traveled = time_hold_button * travel_time
            # print(f'distance_traveled: {distance_traveled}')
            if distance_traveled > record_distance:
                number_of_ways += 1
            # print()
        best_ways.append(number_of_ways)
        multiplication_best_ways *= number_of_ways
        print(f'best_ways: {best_ways}')
        print()
        print()

    print(f'multiplication_best_ways: {multiplication_best_ways}')
