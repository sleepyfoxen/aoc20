from collections import defaultdict

with open('inputs/day14', 'r') as f:
    inp = f.read().strip().splitlines()

# inp = '''mask = 000000000000000000000000000000X1001X
# mem[42] = 100
# mask = 00000000000000000000000000000000XXXX
# mem[26] = 1
# mem[100] = 1
# '''.strip().splitlines()


mem = defaultdict(int)
mask = None
for line in inp:
    cmd, val = line.split(' = ')
    if cmd == 'mask':
        mask = val
        continue

    val = int(val)
    addr = int(cmd[4:].split(']')[0])
    # print(addr, val, bin(val))
    
    masked_val = [ None for _ in mask ]
    for i, (vb, mb) in enumerate(zip(format(val, '036b')[::-1], mask[::-1])):
        if mb == 'X':
            masked_val[-1-i] = vb
        
        elif mb == '1':
            masked_val[-1-i] = '1'
        
        else:
            masked_val[-1-i] = '0'
    

    # print(''.join(masked_val))
    # print(mem)
    mem[addr] = int(''.join(masked_val), 2)
    
print(sum(mem.values()))


mem = defaultdict(int)
mask = None
for line in inp:
    cmd, val = line.split(' = ')
    if cmd == 'mask':
        mask = val
        continue

    val = int(val)
    addr = int(cmd[4:].split(']')[0])
    print(addr, val, bin(val))
    
    masked_val = [ None for _ in mask ]
    for i, (vb, mb) in enumerate(zip(format(addr, '036b')[::-1], mask[::-1])):
        if mb == 'X':
            masked_val[-1-i] = 'X'
        
        elif mb == '1':
            masked_val[-1-i] = '1'
        
        elif mb == '0':
            masked_val[-1-i] = vb
    

    print(''.join(masked_val))
    mask_untainted = ''.join(masked_val)
    highest_mask = ''.join(masked_val)
    masks = []
    masks_n = 2**mask_untainted.count('X')
    # print(masks_n)
    for i in range(masks_n):
        eep = format(i, '0{}b'.format(mask_untainted.count('X')))
        mask_working = ''.join(masked_val)
        for c in eep:
            cnt = 0
            for v in mask_untainted:
                if v == 'X':
                    mask_working = mask_working.replace('X', eep[cnt], 1)
                    cnt += 1
        masks.append(mask_working)

    print()
    if len(masks) != masks_n:
        print('aaaaaaaaaaaaaaaaaaaaaa')
        raise
    # for mask in masks: print(mask)

    for mask_ in masks:
        print(mask_, int(mask_, 2), val)
        mem[int(mask_, 2)] = val

    print('\n\n')

    # while 'X' in lowest_mask:
    #     ll, x, lr = lowest_mask.partition('X')
    #     rl, x, rr = highest_mask.partition('X')
    #     # if r == '':
    #     #     masks.add()
    #     masks.add(ll + '0' + lr.replace('X', '0'))
    #     masks.add(ll + '1' + lr.replace('X', '1'))
    #     masks.add(rl + '0' + lr.replace('X', '0'))
    #     masks.add(rl + '1' + lr.replace('X', '1'))
    #     masks.add(rl.replace('X', '0') + '0' + rr.replace('X', '0'))
    #     masks.add(rl.replace('X', '1') + '1' + rr.replace('X', '1'))
    #     masks.add(ll.replace('X', '0') + '0' + lr.replace('X', '0'))
    #     masks.add(ll.replace('X', '1') + '1' + lr.replace('X', '1'))
    #     lowest_mask = lowest_mask.replace('X', '0', 1)
    #     highest_mask = highest_mask.replace('X', '1', 1)

    #     if '0000000000000000000000000000001' in masks:
    #         print('???')
        # highest_mask = highest_mask.replace('X', '1', 1)
        # if rr == '':
        #     masks.add(highest_mask)
        #     masks.add(lowest_mask)

    # rbits = set()
    # while 'X' in lowest_mask:


    # for c in lowest_mask[::-1]:
    #     # print(c)
    #     if c == 'X':
    #         l, x, r = lowest_mask.partition('X')
    #         masks.add(l + '0' + r)
    #         masks.add(l + '1' + r)


    # print(masks, len(masks))

    # mem[addr] = int(''.join(masked_val), 2)
    
print(sum(mem.values()))


# def awoo(m: str, ms=set()):
#     while 'X' in m:
#         l, x, r = m.partition('X')
#         return ms | awoo(l + '0' + r) | awoo(l + '1' + r)
    
#     ms.add(m)
#     return ms
