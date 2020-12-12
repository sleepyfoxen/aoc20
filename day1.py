import itertools

with open('inputs/day1', 'r') as f:
    input_ = f.read().strip().splitlines()

input_ = sorted(map(int, input_))
for x in input_:
    y = 2020 - x
    if y in input_:
        print(x * y)
        break

for x, y, z in itertools.permutations(input_, 3):
    if x + y + z == 2020:
        print(x * y * z)
        break
