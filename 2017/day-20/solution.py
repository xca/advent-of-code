import re

class Vector:
    def __init__(self,xi,yi,zi):
        self.x = xi
        self.y = yi
        self.z = zi
    def addup(self,v2):
        self.x += v2.x
        self.y += v2.y
        self.z += v2.z
        return self
    def mdist(self):
        return (abs(self.x)+abs(self.y)+abs(self.z))
class Particle:
    def __init__(self,pv,vv,av):
        self.p = pv
        self.v = vv
        self.a = av
    def update(self):
        self.v = self.v.addup(self.a)
        self.p = self.p.addup(self.v)
        # print("after addup, p is:",self.p.x,self.p.y, self.p.z)

        return self
    def mdistance(self):
        return self.p.mdist()
    def format(self):
        return (str(self.p.x)+str(self.p.y)+str(self.p.z))


def part1():
    programInput = open('input.txt','r').read().strip()
    lines = programInput.splitlines()
    pattern = re.compile(r"p=\<(-?\d+),(-?\d+),(-?\d+)\>, v=\<(-?\d+),(-?\d+),(-?\d+)\>, a=\<(-?\d+),(-?\d+),(-?\d+)\>")
    particles = []
    for line in lines:
        # print(line)
        m = pattern.match(line)
        # print(m.group(1))
        p1 = Vector(int(m.group(1)), int(m.group(2)), int(m.group(3)))
        v1 = Vector(int(m.group(4)), int(m.group(5)), int(m.group(6)))
        a1 = Vector(int(m.group(7)), int(m.group(8)), int(m.group(9)))
        particle1 = Particle(p1,v1,a1)
        # print(particle1.format())
        particles.append(particle1)
    i = 0
    closet = 999999
    closetIndex = len(particles) + 1
    while i < 500:
        i += 1
        
        closetOneRun = 999999
        closetIndexOneRun = len(particles) + 1
        for ind, part in enumerate(particles):
            #print("particle index in particles:",ind)
            d = part.mdistance()
            # print(ind,"before update:",part.p.x,part.p.y,part.p.z,)
            # print(ind,"distance is:",d)
            if d < closetOneRun:
                closetOneRun = d
                closetIndexOneRun = ind
            part.update()
            # print(ind,"after update:",part.p.x,part.p.y,part.p.z,)
        if closetIndex == closetIndexOneRun:
            # print(i,"rounds the closed particle doesnot change")
            continue
        else:
            closetIndex = closetIndexOneRun
            closet = closetOneRun
    print("closest particle is",closetIndex,"distance is:",closet)

def part2():
    programInput = open('input.txt','r').read().strip()
    lines = programInput.splitlines()
    pattern = re.compile(r"p=\<(-?\d+),(-?\d+),(-?\d+)\>, v=\<(-?\d+),(-?\d+),(-?\d+)\>, a=\<(-?\d+),(-?\d+),(-?\d+)\>")
    particles = []
    for line in lines:
        # print(line)
        m = pattern.match(line)
        # print(m.group(1))
        p1 = Vector(int(m.group(1)), int(m.group(2)), int(m.group(3)))
        v1 = Vector(int(m.group(4)), int(m.group(5)), int(m.group(6)))
        a1 = Vector(int(m.group(7)), int(m.group(8)), int(m.group(9)))
        particle1 = Particle(p1,v1,a1)
        # print(particle1.format())
        particles.append(particle1)
    i = 0
    while i < 100:
        i += 1
        positions = {}
        for ind, part in enumerate(particles):
            pos = ','.join([str(part.p.x),str(part.p.y),str(part.p.z)])
            if pos in positions:
                # print("existed position",pos,ind)
                positions[pos].append(ind)
            else:
                positions[pos]=[ind]
            part.update()
        delPool = []
        for k,v in positions.items():
            if len(v) > 1:
                delPool += v
        delPool.sort(reverse=True)
        for index in delPool:
            del particles[index]
        #print("after",i,"round, only",len(particles),"left")
    print("Part 2:",len(particles))


def main():
    part1()
    part2()
if __name__ =="__main__":
  main()
            






