
with open('inputs/day5', 'r') as f:
    input_ = f.read().strip().splitlines()

# input_ = ['FBFBBFFRLR', 'BFFFBBFRRR', 'FFFBBBFRRR', 'BBFFBBFRLL']

highest_res = 0
seat_ids = []
for line in input_:
    row_upper = 127
    row_lower = 0
    col_upper = 7
    col_lower = 0

    for c in line:
        if c == 'F':
            row_upper = (row_lower + row_upper) // 2
        if c == 'B':
            row_lower = (row_lower + row_upper) // 2
        if c == 'L':
            col_upper = (col_lower + col_upper) // 2
        if c == 'R':
            col_lower = (col_lower + col_upper) // 2
    
    res = row_upper * 8 + col_upper
    seat_ids.append(res)
    if res > highest_res:
        highest_res = res

print(highest_res)
seat_ids = sorted(seat_ids)
for i, seat in enumerate(seat_ids):
    if seat == seat_ids[i + 1] - 2:
        print(seat + 1)
        break
