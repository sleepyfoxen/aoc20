import itertools

with open('inputs/day9', 'r') as f:
    input_ = f.read().strip().splitlines()

# input_ = '''35
# 20
# 15
# 25
# 47
# 40
# 62
# 55
# 65
# 95
# 102
# 117
# 150
# 182
# 127
# 219
# 299
# 277
# 309
# 576'''.strip().splitlines()

working_numbers = list()
invalids = list()

for line in input_:
    num = int(line)
    if len(working_numbers) < 25:
        working_numbers.append(num)
        continue

    for x, y in itertools.permutations(working_numbers, 2):
        if x + y == num:
            break
    
    else:
        invalids.append(num)
    
    working_numbers.pop(0)
    working_numbers.append(num)
    
print('invalid:', invalids)
target = invalids[0]


for i, line in enumerate(input_):
    num = int(line)
    tmp = num
    sum_numbers = list()
    sum_numbers.append(num)
    j = 1
    if num == target:
        continue

    while tmp <= target:
        if tmp == target:
            print(sum_numbers)
            print(max(sum_numbers), '+', min(sum_numbers), '=', max(sum_numbers) + min(sum_numbers))
            break

        next_ = int(input_[i + j])
        tmp += next_
        sum_numbers.append(next_)
        j += 1

