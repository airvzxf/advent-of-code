# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def get_all_seeds(seeds: tuple) -> list:
    all_seeds = []
    seeds_size = len(seeds)
    for index in range(0, seeds_size // 2 + 1, 2):
        all_seeds += list(range(seeds[index], seeds[index] + seeds[index + 1]))

    return all_seeds


def get_destination(source: int, source_to_destination: tuple) -> int:
    for row in source_to_destination:
        current_destination = row[0]
        current_source = row[1]
        current_range = row[2]
        if current_source <= source <= current_source + current_range - 1:
            current_diff = current_destination - current_source
            return source + current_diff

    return source


if __name__ == '__main__':
    seeds = (
        79, 14, 55, 13
    )

    seed_to_soil = (
        (50, 98, 2),
        (52, 50, 48)
    )

    soil_to_fertilizer = (
        (0, 15, 37),
        (37, 52, 2),
        (39, 0, 15),
    )

    fertilizer_to_water = (
        (49, 53, 8),
        (0, 11, 42),
        (42, 0, 7),
        (57, 7, 4),
    )

    water_to_light = (
        (88, 18, 7),
        (18, 25, 70),
    )

    light_to_temperature = (
        (45, 77, 23),
        (81, 45, 19),
        (68, 64, 13),
    )

    temperature_to_humidity = (
        (0, 69, 1),
        (1, 0, 69),
    )

    humidity_to_location = (
        (60, 56, 37),
        (56, 93, 4),
    )

    complete_table = []

    print('Getting all seeds.')
    complete_table = get_all_seeds(seeds)
    # print(f'complete_table: {complete_table}')
    print(f'Size of seeds: {len(complete_table)}')
    print('Got all seeds.')

    table_loop = (
        (seed_to_soil, 'seed/soil'),
        (soil_to_fertilizer, 'soil/fertilizer'),
        (fertilizer_to_water, 'fertilizer/water'),
        (water_to_light, 'water/light'),
        (light_to_temperature, 'light/temperature'),
        (temperature_to_humidity, 'temperature/humidity'),
        (humidity_to_location, 'humidity/location'),
    )

    table_loop_size = len(table_loop) - 1
    for key, value in enumerate(table_loop):
        print('Start new loop element for the table')
        data, description = value
        print(f'  Process: {description}')
        for index, row in enumerate(complete_table):
            source = row
            destination = get_destination(source, data)
            # print(f'{description}: {source} -> {destination}')
            complete_table[index] = destination

    print()
    print(f'The lowest location is: {min(complete_table)}')
