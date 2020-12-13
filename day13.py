import math
import numpy as np

with open('inputs/day13', 'r') as f:
    inp = f.read().strip().splitlines()

# inp = '''939
# 7,13,x,x,59,x,31,19'''.strip().splitlines()

# inp = '''0
# 17,x,13,19'''.strip().splitlines()

# inp = '''0
# 1789,37,47,1889'''.strip().splitlines()

t, busses = inp
t = int(t)

soonest = 1e10
best_bus = None
for bus in busses.split(','):
    if bus == 'x':
        continue

    bus = int(bus)
    next_bus = math.ceil(t / bus) * bus
    if next_bus < soonest:
        soonest = next_bus
        best_bus = bus


print(best_bus, soonest, soonest - t)
print((soonest - t) * best_bus)

constraints = []

for td, bus in enumerate(busses.split(',')):
    if bus == 'x':
        # print('no restrictions on t+{}'.format(td))
        continue

    # print('bus {} must depart at t+{}'.format(bus, td))
    constraints.append((int(bus), td))

print(constraints)

# for bus, td in constraints:
#     print('0=k+{}mod{},'.format(td, bus))

print(next(zip(*constraints)))
N = np.lcm.reduce(next(zip(*constraints)))
# print(N)
s = r = 0
for bus, td in constraints:
    # 0 = k + td, mod bus

    # calculate bi
    Ni = N/bus
    Ni = int(Ni)
    bi = pow(Ni, -1, bus)

    # print(bi, Ni, bi * Ni, td)
    r += td * bi * Ni
    s += bi * Ni

# print(s, r)
print((r - N - 2 * (r * s % N)) % N)

# inc = i = constraints[0][0]
# while True:
#     for bus, td in constraints:
#         print(i, td, bus, (i + td) % int(bus))
#         if not (i + td) % int(bus) == 0:
#             break
#     else:
#         print(i)
#         break

#     # if all(i % (int(bus) + td) == 0 for bus, td in constraints):
#     #     break
#     i += inc
    

# print(i)

# 35 = x (mod 41)
# 41 = x (mod 35)
# 