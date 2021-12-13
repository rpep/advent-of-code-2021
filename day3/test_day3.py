import textwrap

from day2 import part1, part2

input = textwrap.dedent("""\
         forward 5
         down 5
         forward 8
         up 3
         down 8
         forward 2
         """).split('\n')

def test_part_1():
    assert part1(input) == 150

def test_part_2():
    assert part2(input) == 900

