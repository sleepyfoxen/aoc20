from itertools import product

with open('inputs/day11', 'r') as f:
    inp = f.read().strip().splitlines()

# inp = '''L.LL.LL.LL
# LLLLLLL.LL
# L.L.L..L..
# LLLL.LL.LL
# L.LL.LL.LL
# L.LLLLL.LL
# ..L.L.....
# LLLLLLLLLL
# L.LLLLLL.L
# L.LLLLL.LL
# '''.strip().splitlines()

next_inp = None

# while True:
#     next_inp = inp.copy()
#     for y, line in enumerate(inp):
        
#         # for line in inp:
#         #     print(line)

#         new_line = list(line)
#         for x, seat in enumerate(line):
#             if seat == '.':
#                 continue

#             if seat == 'L':
#                 occupied = list()
#                 for dy, dx in product((-1, 0, 1), repeat=2):
#                     if y + dy < 0 or y + dy >= len(inp):
#                         continue
#                     if x + dx < 0 or x + dx >= len(line):
#                         continue

#                     occupied.append(inp[y+dy][x+dx] == '#')

#                 if any(occupied):
#                     continue
                
#                 else:
#                     new_line = list(new_line)
#                     new_line[x] = '#'
#                     new_line = ''.join(new_line)
#                     next_inp[y] = new_line
            
#             if seat == '#':
#                 occupied = list()
#                 for dy, dx in product((-1, 0, 1), repeat=2):
#                     if y + dy < 0 or y + dy >= len(inp):
#                         continue
#                     if x + dx < 0 or x + dx >= len(line):
#                         continue
#                     if dy == dx == 0:
#                         continue

#                     occupied.append(inp[y+dy][x+dx] == '#')

#                 if len(list(filter(None, occupied))) >= 4:
#                     new_line = list(new_line)
#                     new_line[x] = 'L'
#                     new_line = ''.join(new_line)
#                     next_inp[y] = new_line                

#     for line in next_inp:
#         print(line)

#     print()

#     if inp == next_inp:
#         break

#     inp = next_inp
# # print(next_inp)

# count = 0
# for line in inp:
#     for c in line:
#         if c == '#':
#             count += 1

# print(count)


# inp = '''.......#.
# ...#.....
# .#.......
# .........
# ..#L....#
# ....#....
# .........
# #........
# ...#.....'''.strip().splitlines()

# inp = '''.##.##.
# #.#.#.#
# ##...##
# ...L...
# ##...##
# #.#.#.#
# .##.##.'''.strip().splitlines()

while True:
    next_inp = inp.copy()
    for y, line in enumerate(inp):
        
        # for line in inp:
        #     print(line)

        new_line = list(line)
        for x, seat in enumerate(line):
            if seat == '.':
                continue

            if seat == 'L':
                occupied = list()
                for dy, dx in product((-1, 0, 1), repeat=2):
                    if y + dy < 0 or y + dy >= len(inp):
                        continue
                    if x + dx < 0 or x + dx >= len(line):
                        continue
                    if dy == dx == 0:
                        continue

                    ddy, ddx = dy, dx
                    while inp[y+ddy][x+ddx] not in ('L', '#'):
                        if y + ddy == -1 or (dy > 0 and (y + ddy >= len(inp) - 1)):
                            break
                        if x + ddx == -1 or (dx > 0 and (x + ddx >= len(line) - 1)):
                            break
                        ddy += dy
                        ddx += dx
                    
                    occupied.append(inp[y+ddy][x+ddx] == '#')

                if any(occupied):
                    continue
                
                else:
                    new_line = list(new_line)
                    new_line[x] = '#'
                    new_line = ''.join(new_line)
                    next_inp[y] = new_line
            
            if seat == '#':
                occupied = list()
                for dy, dx in product((-1, 0, 1), repeat=2):
                    if y + dy < 0 or y + dy >= len(inp):
                        continue
                    if x + dx < 0 or x + dx >= len(line):
                        continue
                    if dy == dx == 0:
                        continue

                    ddy, ddx = dy, dx
                    while inp[y+ddy][x+ddx] not in ('L', '#'):
                        if y + ddy == -1 or (dy > 0 and (y + ddy >= len(inp) - 1)):
                            break
                        if x + ddx == -1 or (dx > 0 and (x + ddx >= len(line) - 1)):
                            break
                        ddy += dy
                        ddx += dx

                    
                    # if y == 1 and x == 0:
                    #     print('awooga')
                    
                    if y+ddy < 0 or x+ddx < 0:
                        occupied.append(False)

                    else:
                        occupied.append(inp[y+ddy][x+ddx] == '#')

                if len(list(filter(None, occupied))) >= 5:
                    new_line = list(new_line)
                    new_line[x] = 'L'
                    new_line = ''.join(new_line)
                    next_inp[y] = new_line                

    for line in next_inp:
        print(line)

    print()

    if inp == next_inp:
        break

    inp = next_inp

count = 0
for line in inp:
    for c in line:
        if c == '#':
            count += 1

print(count)
