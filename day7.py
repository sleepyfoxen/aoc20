with open('inputs/day7', 'r') as f:
    input_ = f.read().strip().splitlines()


containers = set(['shiny gold'])
old_len = len(containers)

while True:
    containers_2 = set()
    for line in input_:
        left, right = line.split(' contain ')
        colour = ' '.join(left.split(' ')[:2])
        for contents in right.split(','):
            contents = contents.strip()
            for e in containers:
                if e in contents:
                    containers_2.add(colour)

        containers = containers.union(containers_2)

    if len(containers) == old_len:
        break
    old_len = len(containers)

print(len(containers) - 1)


def r(c: str) -> int:
    for line in input_:
        left, right = line.split(' contain ')
        colour = ' '.join(left.split(' ')[:2])
        if colour == c:
            nexts = list()
            cnts = list()
            for n in right.split(','):
                n = n.strip()
                if 'no other bags' in n: return 0
                cnt = int(n[0])
                next_ = ' '.join(n.split(' ')[1:3])
                cnts.append(cnt)
                nexts.append(next_)

            return sum(cnts) + sum([cnts[i] * r(nexts[i]) for i in range(len(nexts))])
        
    return 0


print(r('shiny gold'))
