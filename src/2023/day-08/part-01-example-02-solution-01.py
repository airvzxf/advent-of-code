#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
Solution of the AoC 2023. Day 8, part 1 and it is the solution of the example.
"""


def get_index_instructions(instructions: str) -> list:
    index_instructions = []
    for instruction in instructions:
        if instruction.upper() == "L":
            index_instructions.append(0)
        else:
            index_instructions.append(1)
    return index_instructions


def get_steps_to_last_node(first_node: str, nodes: dict, index_instructions: list) -> int:
    total_instructions = len(index_instructions)
    print(f'total_instructions: {total_instructions}')
    print()

    current_node = first_node
    index = 0
    steps = 0
    while True:
        print(f'index_instructions[{index}]: {index_instructions[index]}')
        current_instruction = index_instructions[index]
        print(f'current_instruction: {current_instruction}')
        print(f'current_node: {current_node}')
        print(f'nodes[current_node]: {nodes[current_node]}')
        current_node = nodes[current_node][current_instruction]
        print(f'current_node: {current_node}')
        steps += 1
        print(f'steps: {steps}')
        if current_node == 'ZZZ':
            return steps
        index += 1
        print(f'index: {index}')
        if index == total_instructions:
            index = 0
            print(f'index: {index}')
        print()


if __name__ == "__main__":
    instructions = 'LLR'
    first_node = 'AAA'
    nodes = {
        'AAA': ('BBB', 'BBB'),
        'BBB': ('AAA', 'ZZZ'),
        'ZZZ': ('ZZZ', 'ZZZ'),
    }
    index_instructions = get_index_instructions(instructions)
    print(f'index_instructions: {index_instructions}')
    steps = get_steps_to_last_node(first_node, nodes, index_instructions)
    print(f'steps: {steps}')
