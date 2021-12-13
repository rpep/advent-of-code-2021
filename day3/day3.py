import os
import numpy as np


def load_data(filename):
    data = np.loadtxt('input.txt', delimiter='')
    return data


def gamma_rate(data):
    n = len(data)
    return (np.sum(data, axis=1) < n/2) * 1


def epsilon_rate(gamma):
    return ~gamma

def part1(data):
    gamma = gamma_rate(data)
    epsilon = epislon_rate(gamma)
    return gamma * epsilon

if __name__ == '__main__':
    array = load_data('input.txt')
    print(f"Part 1 answer = {part1(array)}")
    print(f"Part 2 answer = {part2(array)}")
