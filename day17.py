from itertools import product

with open('inputs/day17', 'r') as f:
    inp = f.read().strip().splitlines()

ones = set()

origin_delta = None
for x, row in enumerate(inp):
    for y, bit in enumerate(row):
        if bit == '#':
            ones.add((x, y, 0, 0))

asdf = list(product((-1, 0, 1), repeat=4))

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
f(ones)
