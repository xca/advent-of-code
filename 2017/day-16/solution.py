from copy import deepcopy

def spin(p,i):
    s = len(p)-i
    p1 = p[s:] + p[:s]
    return p1

def exchange(p,a,b):
    p[a],p[b] = p[b],p[a]
    return p

def partner(p,a,b):
    ai = 20
    bi = 20
    for i,t in enumerate(p):
        if t == a:
            ai = i
        if t == b:
            bi = i
    p = exchange(p,ai,bi)
    return p

def dance(programs,cmds):
#programInput = open('input_example.txt', 'r').read().strip()
    for cmd in cmds:
        if cmd[0] == 's':
            programs = spin(programs,int(cmd[1:]))
        if cmd[0] == 'x':
            c = cmd[1:].split('/')
            programs = exchange(programs,int(c[0]),int(c[1]))
        if cmd[0] == 'p':
            c = cmd[1:].split('/')
            programs = partner(programs,c[0],c[1])
    return programs

def part1(programInput):
    cmds = programInput.split(',')
    programs = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p']
    programs = dance(programs,cmds)
    print("Part 1:",''.join(programs))

def part2(programInput):
    cmds = programInput.split(',')
    programs = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p']
    results = []
    progs = deepcopy(programs)
    # results.append(''.join(progs))
    while True:
        progs = dance(progs,cmds)
        strProgs = ''.join(progs)
        if strProgs in results:
            break
        else:
            results.append(strProgs)
    times = 1000000000 % len(results)
    print("total Results:",len(results))
    print("times:",times)
    for i in range(times):
        programs = dance(programs,cmds)
    print("Part 2:",''.join(programs))
    

def main():
    programInput = open('input.txt', 'r').read().strip()
    part1(programInput)
    part2(programInput)

if __name__ =="__main__":
  main()
# programInput = open('input.txt', 'r').read().strip()
# cmds = programInput.split(',')
# programs = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p']


# print(cmds)
# 
# print("original programs",programs)
# programs = spin(programs,1)
# print("after spin:",programs)
# programs = swap(programs,3,4)
# print("after swap:",programs)
# programs = partner(programs,'e','b')
# print("after partner:",programs)