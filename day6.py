import string

with open('inputs/day6', 'r') as f:
    input_ = f.read().strip().split('\n\n')

# input_ = '''abc

# a
# b
# c

# ab
# ac

# a
# a
# a
# a

# b'''.strip().split('\n\n')

part1 = 0
for group in input_:
    group = set(group)
    group.discard('\n')
    part1 += len(group)

print(part1)
print()

part2 = 0
for group in input_:
    common = set(string.ascii_letters)
    for person in group.splitlines():
        common.intersection_update(set(person))

    part2 += len(common)

print(part2)
