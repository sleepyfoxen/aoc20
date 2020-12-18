inp = '5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))'
inp = '1 + 2 * 3 + 4 * 5 + 6'
inp = '((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2'
inp = '11664 + 2 + 4 * 2'
inp = '5 + (8 * 3 + 9 + 3 * 4 * 3)'

with open('inputs/day18', 'r') as f:
    qu = f.read().strip().splitlines()


def solve(inp):
    rb = inp.find(')')
    if rb == -1:
        # print('no more groups:', inp)
        parts = inp.split(' ')
        ans = eval(''.join(parts[0:3]))
        # print(ans)
        for i in range(3, len(parts), 2):
            # print(parts[i:i+2])
            ans = eval('{} {}'.format(ans, ''.join(parts[i:i+2])))
            # print(ans)
        return ans
    
    lb = rb - inp[rb::-1].find('(')
    # print(inp, lb, rb)
    bg_ = solve(inp[lb+1:rb])
    inp = inp.replace(inp[lb:rb+1], str(bg_))
    # print(inp)

    return solve(inp)

sum_ = 0
for line in qu:
    sum_ += solve(line)
print(sum_)

import re

def solveb(inp):
    rb = inp.find(')')
    if rb == -1:
        # print('no more groups:', inp)
        ss = re.sub(r'(\d+) \+ (\d+)', r'(\1 + \2)', inp)
        ss = re.sub(r'(.*) \+ (\d+)', r'(\1 + \2)', ss)
        ss = re.sub(r'([^\*]+) \+ (\d+)', r'(\1 + \2)', ss)
        ans = eval(ss)
        # print(ss, '=', ans)
        return ans
    
    lb = rb - inp[rb::-1].find('(')
    # print(inp)
    bg_ = solveb(inp[lb+1:rb])
    inp = inp.replace(inp[lb:rb+1], str(bg_))
    # print(inp)

    return solveb(inp)

sum_ = 0
for line in qu:
    sum_ += solveb(line)
print(sum_)