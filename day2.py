with open('inputs/day2', 'r') as f:
    input_ = f.read().strip().splitlines()

# input_ = '''1-3 a: abcde
# 1-3 b: cdefg
# 2-9 c: ccccccccc'''.strip().splitlines()

valid_1 = 0
valid_2 = 0
for p in input_:
    n, c, pwd = p.split(' ')
    n_l, n_h = map(int, n.split('-'))
    c = c[0]

    if n_l <= pwd.count(c) <= n_h:
        valid_1 += 1

    n_l -= 1
    n_h -= 1

    try:
        if (pwd[n_l] == c) ^ (pwd[n_h] == c):
            valid_2 += 1
    except IndexError:
        try:
            if pwd[n_l] == c: valid_2 += 1
        except: pass


print(valid_1, valid_2)
