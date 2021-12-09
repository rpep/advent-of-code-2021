import os
import numpy as np


def load_data(filename):
    return np.loadtxt(filename)


def part1(array):
    return np.sum(np.diff(array) > 0)

def part2(array):
    return np.sum(np.diff(np.convolve(array, np.ones(3))[2:-2]) > 0)
    

if __name__ == '__main__':
    array = load_data('input.txt')
    print(f"Part 1 answer = {part1(array)}")
    print(f"Part 2 answer = {part2(array)}")
