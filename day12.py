import cmath
import math

with open('inputs/day12', 'r') as f:
    inp = f.read().strip().splitlines()

loc = 0+0j
way = 1+10j
for thing in inp:
    cmd, val = thing[0], int(thing[1:])
    if cmd == 'F':
        loc += val * way
    
    if cmd == 'N':
        way += val * (1 + 0j)
    
    if cmd == 'S':
        way += val * (-1 + 0j)
    
    if cmd == 'E':
        way += val * (0 + 1j)
    
    if cmd == 'W':
        way += val * (0 - 1j)
    
    if cmd == 'R':
        way_ = cmath.phase(way)
        way_ += math.radians(val)
        way = cmath.rect(abs(way), way_)

    if cmd == 'L':
        way_ = cmath.phase(way)
        way_ -= math.radians(val)
        way = cmath.rect(abs(way), way_)

    print('loc: {:.0f}, way: {:.0f}'.format(loc, way))

print(round(abs(loc.imag) + abs(loc.real)))
