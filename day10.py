from collections import defaultdict
from math import factorial

def ncr(n, r):
    if n < r: return 0
    return factorial(n) / (factorial(r) * factorial(n - r))

with open('inputs/day10', 'r') as f:
    inp = sorted(map(int, f.read().strip().splitlines() + [0]))

def p1(inp):
    d = defaultdict(int)
    for i, j in zip(inp, inp[1:]):
        d[j - i] += 1
    
    return d

# print(p1(inp))

def aaaa(inp, count=1):
    # print(inp, 'cnt', count)
    # print('count', count)
    if len(inp) <= 2:
        return count
    
    y, z = inp[-2:]
    # print(y, z)
    if z - y == 3:
        return aaaa(inp[:-1], count)
    
    # check how many 1s in a row we have
    n = 2
    while inp[-n] - inp[-n-1] == 1:
        n += 1
        if inp[-n-1] == 0:
            n += 1
            break

    k = n - 2

    inc = ncr(k, 2) + ncr(k, 1) + 1
    count *= inc

    print('{} ones, k={}, inc={}, count={}'.format(n, k, inc, count))


    # print('add {} possibilities'.format(inc))
    # print('count =', count)

    return aaaa(inp[:-n], count=count)

    # if inc == 0:
    #     return aaaa(inp[:-n], count=count)

    # return aaaa(inp[:-n], count=count) # + aaaa(inp[:-n], k)
    

# print(ncr(3, 2))
# print(ncr(3, 1))
# inp = sorted(map(int, '''16
# 0
# 10
# 15
# 5
# 1
# 11
# 7
# 19
# 6
# 12
# 4'''.strip().splitlines()))
print(aaaa(inp))

inp = sorted(map(int, '''28
0
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3'''.strip().splitlines()))
# print(aaaa(inp))
# print(inp)

# def npr(n, r):
#     if n < r: return 0
#     return factorial(n) / factorial(n - r)

# from collections import defaultdict
# import itertools

# from math import comb
# input_ = list(input_)
# input_.append(0)
# input_.append(max(input_) + 3)
# inp = sorted(input_)
# diffs = defaultdict(int)
# for i, j in zip(inp, inp[1:]):
#     diffs[j-i] += 1

# print(diffs)

# def ways(inp_: list):
#     # n = 0
#     # for i, j in zip(inp_, inp_[1:]):

#     #     if j - i == 1:
#     #         if i + 3 in inp_:
#     #             n += 1
#     #         if i + 2 in inp_:
#     #             n += 1

#     #         print(n)
            
#     #         inp__ = inp_.copy()
#     #         inp__.remove(i)
#     #         print(inp__)
#     #         return n + ways(inp__)
        
#     # return 1

#     n = 0
#     total = 1
#     for i, j in zip(inp_, inp_[1:]):
#         last_n = n
#         if j - i == 1:
#             if i + 3 in inp_:
#                 n += 1
#             if i + 2 in inp_:
#                 n += 1
#             # if n - last_n > 0:
#             #     total += comb()

#         # print(i, j, n, n - last_n, total)



# # print(ways(inp))

# from sys import stdout

# def aaaaa(inp: list, step=1):
#     n = 1
#     print(inp)

#     #' base case
#     # if all(j - i == 1 for i, j in zip(inp[:-1], inp[1:-1])):
#     #     print('base path, {}'.format(inp))
#     #     return n
#     if len(inp) < 4: return n
    
#     # len >= 3: xyz
#     x, y, z = inp[-3:]

#     print(x, y, z)

#     if z - y == 3:
#         return aaaaa(inp[:-1])
    
    
#     return 2 * aaaaa(inp[:-3]) 
    
#     # okay z - y = 1
#     # if z - y == 2:
#     #     print('z - y = 2???')

#     # if z - x == 4:
#     #     return 2 * aaaaa(inp[:-2])

#     # if z - w == 5:
#     #     return 3 + aaaaa(inp[:-3])

#     # if z - w == 4:
#     #     return 

#     # if z - w == 3:
#     #     return 0 + aaaaa(inp[:-4])
    
#     # # if z - x == 3:
#     # #     return 2 * aaaaa(inp[:-1])

#     # if z - w > 3:
#     #     return 2 * aaaaa(inp[:-1])


#     # if z - x == 1:
#     #     return 2 * aaaaa(inp[:-2])

#     # return 2 * aaaaa(inp[:-1])

#     # c = inp[-1] - inp[-2]
#     # if c == 3:
#     #     return aaaaa(inp[:-1])  # does not add to the tree

#     # if c == 2:
#     #     print('c = 2?')
#     #     # if inp[-3] - inp[-2] == 1:
#     #     #     return 2 * aaaaa(inp[:-2])
#     #     # else:
#     #     #     return aaaaa(inp[:-1])

#     # if c == 1:
#     #     if inp[-3] - inp[-2] == 3:
#     #         return aaaaa(inp[:-2])
#     #     else:
#     #         return aaaaa(inp[:-2]) + aaaaa(inp[:-1])


#     #' recursive case
#     # okay we must have to process multiple paths somewhere
#     # lets split that into cases



#     # cases = set()
#     # for idx, (i, j) in enumerate(zip(inp, inp[1:])):

#         # at each stage i have to:




#         # y = False
#         # # last_n = n
#         # # if j - i == 3:
#         #     # ret = aaaaa(inp[idx+1:])
#         # print('{}->{} {} {} ({}, {})'.format(inp, inp[idx+1:], idx, n, i, j))

#         # if j - i == 1:
#         #     if i + 2 in inp:
#         #         n += aaaaa(inp[idx+1:])
#         #         y = True
#         #         # break
#         #     if i + 3 in inp:
#         #         if y:
#         #             n += aaaaa(inp[idx+2:])
#         #         else:
#         #             n += aaaaa(inp[idx+1:])
#         #         break
#         # if j - i == step:
#         #     if j - i + 1 in inp:
#         #         n += aaaaa(inp[idx+step:], step=step+1)

#             # return ret
#         # if j - i == 1:
#         #     if i + 3 in inp:
#         #         n += 1
#         #     if i + 2 in inp:
#         #         n += 1

#         #     if n == 1:
#         #         ret = aaaaa(inp[idx+1:])
#         #         print('{}->{} {} {} {} {} ret: {}'.format(inp, inp[idx+1:], idx, n, i, j, ret))
#         #         return ret

#         #     if n == 2:
#         #         ret = n * (aaaaa(inp[idx+1:]) + aaaaa(inp[idx] ++ inp[idx+2:]))
#         #         print('{}->{} {} {} {} {} ret: {}'.format(inp, inp[idx+1:], idx, n, i, j, ret))
#         #         return ret
        

#     return n


# print(aaaaa(inp))
# print()
# inp = [0, 3, 4, 5]
# print(aaaaa(inp))
# inp = [0, 1, 4, 5]
# print(aaaaa(inp))

# paths = set()
# def aaaaaaaa(inp: list, idx_ = 0):
#     # print(idx)
#     for idx, (i, j) in enumerate(zip(inp[idx_:], inp[idx_+1:])):
#         # print(inp[idx:])
#         if j - i == 1:
#         #     # print(aaaaaaaa(inp, idx + 1))
#         #     # inp_ = inp.copy()
#         #     # inp_.pop(idx)
#         #     # aaaaaaaa(inp_, idx)
#         #     # break
#         #     continue
#         # if j - i == 2:
#         #     inp_ = inp.copy()
#         #     inp_.pop(idx)
#         #     aaaaaaaa(inp_, idx)
#         # if j - i == 3:
#         #     inp_ = inp.copy()
#         #     inp_.pop(idx)
#         #     aaaaaaaa(inp_, idx)
    
#             if i + 2 in inp:
#                 inp_ = inp.copy()
#                 inp_.remove(j)
#                 aaaaaaaa(inp_, idx+1)
#             if i + 3 in inp:
#                 inp_ = inp.copy()
#                 inp_.remove(j)
#                 aaaaaaaa(inp_, idx+1)
        
#         if j - i > 3:
#             break

#         if j - i == 3:
#             continue


#     # print(inp)
#     print(inp)
#     paths.add(tuple(inp))
#     return inp

# def a(inp):
#     # thispath = list((inp[0], inp[-1]))
#     thispath = list()
#     for i, n in enumerate(inp[:-1]):
#         if inp[i+1] - inp[i] > 3: break
#         if i == 0: continue
#         thispath.append(n)
#         if n + 1 in inp:
#             inp2 = sorted(thispath.copy())
#             # inp2.remove(n)
#             print(inp[i:], i, inp[i+1:])
#             # inp2.extend(inp[i+1:])
#             # inp2.remove(n)

#             a(inp2)
#         break
    
#     print(sorted(thispath))

# # a(inp)

# def aa(inp):

#     for idx, (i, j) in enumerate(zip(inp, inp[1:])):
#         print('index: {}, this: {}, next: {}'.format(idx, i, j))

# # inp2 = [0, 1, 2, 5]
# # print(inp2)
# # aa(inp2)

# # print(aaaaaaaa(inp))
# # print(paths)
# # print(len(paths))


