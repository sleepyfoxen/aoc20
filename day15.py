from collections import defaultdict

with open('inputs/day15', 'r') as f:
    inp = list(map(int, f.read().strip().split(',')))

d = defaultdict(int)
for i, n in enumerate(inp[:-1]):
    d[n] = i + 1
turn = len(inp) + 1
last = inp[-1]
print(d)
while turn <= 2020:
    speak = 0
    last_spoken = d[last]
    d[last] = turn - 1

    if last_spoken == 0:
        speak = last_spoken
    else:
        speak = abs(turn - last_spoken - 1)

    print(turn, last, last_spoken, speak)
    last = speak
    turn += 1


d = defaultdict(int)
for i, n in enumerate(inp[:-1]):
    d[n] = i + 1
turn = len(inp) + 1
last = inp[-1]
print(d)
while turn <= 30000000:
    speak = 0
    last_spoken = d[last]
    d[last] = turn - 1

    if last_spoken == 0:
        speak = last_spoken
    else:
        speak = abs(turn - last_spoken - 1)

    if turn % 100000 == 0:
        print('num: {}, remain: {}; {}%'.format(turn, 30000000 - turn, turn / 30000000 * 100))
    last = speak
    turn += 1

print(last)
