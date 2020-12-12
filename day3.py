from functools import reduce
from operator import mul
from typing import NewType
Pair = NewType('Pair', (int, int))
def product(l): return reduce(mul, l, 1)

with open('inputs/day3', 'r') as f:
    input_ = f.read().strip().splitlines()

# input_ = '''..##.......
# #...#...#..
# .#....#..#.
# ..#.#...#.#
# .#...##..#.
# ..#.##.....
# .#.#.#....#
# .#........#
# #.##...#...
# #...##....#
# .#..#...#.#'''.strip().splitlines()

def bobsled(vector: Pair) -> int:
    trees = 0
    x = 0
    for y, line in enumerate(input_):
        if y % vector[1] != 0: continue

        if line[x % len(line)] == '#':
            trees += 1
    
        x += vector[0]
    return trees

bobsleds = [bobsled(p) for p in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]]
print(bobsleds)
print(product(bobsleds))
