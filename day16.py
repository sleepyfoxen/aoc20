from collections import defaultdict

with open('inputs/day16', 'r') as f:
    inp = f.read().strip().split('\n\n')


rule_list = []
for rules in inp[0].splitlines():
    name, rule = rules.split(': ')
    tmp = rule.split(' or ')
    rule_list.append([ tuple(map(int, v.split('-'))) for v in tmp ])

invalid = []
invalid_tic = []
d = defaultdict(set)

for t in inp[2].splitlines()[1:]:
    fields = list(map(int, t.split(',')))

    for f in fields:
        for r in rule_list:
            if f in range(r[0][0], r[0][1]+1) or f in range(r[1][0], r[1][1]+1):
                break
        else:
            invalid.append(f)
            invalid_tic.append(t)
    
print(sum(invalid))


d = defaultdict(set)
for t in inp[2].splitlines()[1:]:
    if t in invalid_tic: continue
    fields = list(map(int, t.split(',')))
    
    for i, f in enumerate(fields):

        if len(d[i]) > 0:
            rs = [ rule_list[r_] for r_ in d[i] ]
            d[i].clear()
            for r in rs:
                if f in range(r[0][0], r[0][1]+1) or f in range(r[1][0], r[1][1]+1):
                    d[i].add(rule_list.index(r))
            
        else:
            for j, r in enumerate(rule_list):
                if f in range(r[0][0], r[0][1]+1) or f in range(r[1][0], r[1][1]+1):
                    d[i].add(j)


d2 = defaultdict(set)
d3 = defaultdict(set)
solved = set()
while True:
    for k, vs in d.items():
        vs = vs - solved
        if len(vs) == 1:
            d2[k] = inp[0].splitlines()[list(vs)[0]].split(':')[0]
            d3[k] = list(vs)[0]
            solved.add(d3[k])
    
    if len(solved) == len(d): break

val = 1
for k in sorted(d2):
    if d2[k].startswith('departure'):
        val *= int(inp[1].split(',')[k])

print(val)
