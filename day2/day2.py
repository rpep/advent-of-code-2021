import os
import numpy as np


def load_data(filename):
    f = open(filename, 'r')
    lines = f.read().split('\n')
    return lines

def process(lines):
    return [tuple(line.split(' ')) for line in lines if line]

def part1(lines):
    tuples = process(lines)
    x = 0
    z = 0
    for direction, quantity in tuples:
        if direction == 'forward':
            x += int(quantity)
        if direction == 'down':
            z -= int(quantity)
        if direction == 'up':
            z += int(quantity)
    return -x*z

def part2(lines):
    tuples = process(lines)
    x = 0
    z = 0
    aim = 0
    for direction, quantity in tuples:
        if direction == 'forward':
            x += int(quantity)
            z -= int(quantity)*aim
        if direction == 'down':
            aim += int(quantity)
        if direction == 'up':
            aim -= int(quantity)
    return -x*z

if __name__ == '__main__':
    array = load_data('input.txt')
    print(f"Part 1 answer = {part1(array)}")
    print(f"Part 2 answer = {part2(array)}")
