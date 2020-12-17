from itertools import product

with open('inputs/day17', 'r') as f:
    inp = f.read().strip().splitlines()

ones = list()

origin_delta = None
for x, row in enumerate(inp):
    for y, bit in enumerate(row):
        if bit == '#':
            ones.append((x, y, 0, 0))

asdf = list(product((-1, 0, 1), repeat=4))

def f(ones):
    for i in range(6):
        ones_next = set()
        for v in ones:
            for dx, dy, dz, dw in asdf:
                was_one = bk = False
                counter = 0
                if dx == dy == dz == dw == 0: was_one = True
                nn = (v[0] + dx, v[1] + dy, v[2] + dz, v[3] + dw)
                for dx_, dy_, dz_, dw_ in asdf:
                    if dx_ == dy_ == dz_ == dw_ == 0: continue
                    adj = (nn[0] + dx_, nn[1] + dy_, nn[2] + dz_, nn[3] + dw_)
                    if adj in ones: counter += 1
                    if counter > 3:
                        bk = True
                        break
                if bk: continue
                if counter == 3 or (was_one and (2 <= counter <= 3)): 
                    ones_next.add(nn)

        ones = ones_next
        print(len(ones_next))
print()
f(ones)
