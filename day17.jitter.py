from itertools import product
from numba import njit

with open('inputs/day17', 'r') as f:
    inp = f.read().strip().splitlines()

@njit(fastmath=True, parallel=True, cache=True)
def setup(inp):
    ones = set()
    origin_delta = None
    for x, row in enumerate(inp):
        for y, bit in enumerate(row):
            if bit == '#':
                ones.add((x, y, 0, 0))
    return ones

asdf = tuple(product((-1, 0, 1), repeat=4))

@njit(fastmath=True, parallel=True, cache=True)
def f(ones):
    for i in range(6):
        ones_next = set()
        for v in ones:
            for dx, dy, dz, dw in asdf:
                counter = 0
                was_one = dx == dy == dz == dw == 0
                nn = (v[0] + dx, v[1] + dy, v[2] + dz, v[3] + dw)
                for dx, dy, dz, dw in asdf:
                    if dx == dy == dz == dw == 0: continue
                    adj = (nn[0] + dx, nn[1] + dy, nn[2] + dz, nn[3] + dw)
                    if adj in ones: counter += 1
                    if counter > 3: break
                else:
                    if counter == 3 or (was_one and counter in (2, 3)):
                        ones_next.add(nn)

        ones = ones_next
        print(len(ones_next))
print()
f(setup(inp))

# pip3 install --prefer-binary numba icc_rt
#
#
# fox@rawr:~$ time python3 asdf.py 2>/dev/null
#
# 209
# 185
# 892
# 556
# 2824
# 1868
#
# real	0m0.692s
# user	0m0.744s
# sys	0m0.352s
