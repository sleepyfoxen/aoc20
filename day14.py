from collections import defaultdict

with open('inputs/day14', 'r') as f:
    inp = f.read().strip().splitlines()


mem = defaultdict(int)
mask = None
for line in inp:
    cmd, val = line.split(' = ')
    if cmd == 'mask':
        mask = val
        continue

    val = int(val)
    addr = int(cmd[4:].split(']')[0])
    masked_val = [ None for _ in mask ]
    for i, (vb, mb) in enumerate(zip(format(val, '036b')[::-1], mask[::-1])):
        if mb == 'X':
            masked_val[-1-i] = vb
        elif mb == '1':
            masked_val[-1-i] = '1'
        else:
            masked_val[-1-i] = '0'

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
    masked_val = [ None for _ in mask ]
    for i, (vb, mb) in enumerate(zip(format(addr, '036b')[::-1], mask[::-1])):
        if mb == 'X':
            masked_val[-1-i] = 'X'
        elif mb == '1':
            masked_val[-1-i] = '1'
        elif mb == '0':
            masked_val[-1-i] = vb
    
    mask_untainted = ''.join(masked_val)
    masks = []
    masks_n = 2**mask_untainted.count('X')
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

    for mask_ in masks:
        mem[int(mask_, 2)] = val


print(sum(mem.values()))
