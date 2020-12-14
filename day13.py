import math
import numpy as np

with open('inputs/day13', 'r') as f:
    inp = f.read().strip().splitlines()

t, busses = inp
t = int(t)

soonest = 1e10
best_bus = None
for bus in busses.split(','):
    if bus == 'x': continue
    bus = int(bus)
    next_bus = math.ceil(t / bus) * bus

    if next_bus < soonest:
        soonest = next_bus
        best_bus = bus

print((soonest - t) * best_bus)

constraints = []

for td, bus in enumerate(busses.split(',')):
    if bus == 'x': continue
    constraints.append((int(bus), td))

N = np.lcm.reduce(next(zip(*constraints)))
s = r = 0
for bus, td in constraints:
    # 0 = k + td, mod bus
    Ni = N/bus
    Ni = int(Ni)
    bi = pow(Ni, -1, bus)

    r += td * bi * Ni
    s += bi * Ni

print((r - N - 2 * (r * s % N)) % N)
