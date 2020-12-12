

with open('inputs/day8', 'r') as f:
    input_ = f.read().strip().splitlines()

# input_ = '''
# nop +0
# acc +1
# jmp +4
# acc +3
# jmp -3
# acc -99
# acc +1
# jmp -4
# acc +6'''.strip().splitlines()

def run(inp: list):
    acc = 0
    ip = 0
    visited = set()

    while ip not in visited:
        if ip == len(inp):
            print('terminating')
            print(acc)
            return True
        visited.add(ip)
        inst, arg = inp[ip].split(' ')
        print(inst, arg)

        ip += 1
        if inst == 'acc':
            acc += int(arg)
        elif inst == 'jmp':
            ip += int(arg) - 1

    print('looping')
    print(ip)
    print(acc)

    return False

run(input_)

for i, line in enumerate(input_):
    inst, arg = line.split(' ')
    if inst == 'nop':
        inp = input_.copy()
        inp[i] = 'jmp ' + arg
        if run(inp): break
    if inst == 'jmp':
        inp = input_.copy()
        inp[i] = 'nop ' + arg
        if run(inp): break
