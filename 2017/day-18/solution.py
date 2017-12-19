
def isNumber(s):
  try:
    int(s)
    return True
  except ValueError:
    return False

def part1(lines):
  snd = 0
  x = {}
  totalCmds = len(lines)
  print('totalCmds:',totalCmds)
  i = 0
  while i < totalCmds:
    e= lines[i].split();
    if e[1] not in x:
      x[e[1]]=0
    #print(e[1],':',x[e[1]])
    if e[0] == 'snd':
      print(snd)
      if isNumber(e[1]):
        snd = int(e[1])
      else:
        snd = x[e[1]]
    elif e[0] == 'set':
      if isNumber(e[2]):
        x[e[1]] = int(e[2])
      else:
        x[e[1]] = x[e[2]]
    elif e[0] == 'add':
      if isNumber(e[2]):
        x[e[1]] += int(e[2])
      else:
        x[e[1]] += x[e[2]]
    elif e[0] == 'mul':
      if isNumber(e[2]):
        x[e[1]] *= int(e[2])
      else:
        x[e[1]] *= x[e[2]]
    elif e[0] == 'mod':
      if isNumber(e[2]):
        x[e[1]] = x[e[1]] % int(e[2])
      else:
        x[e[1]] = x[e[1]] % x[e[2]]
    elif e[0] == 'rcv':
      if x[e[1]] == 0:
        i += 1
      else:
        x[e[1]] = snd
        print(i,":",snd)
        break
    elif e[0] == 'jgz':
    #  print(e)
      if x[e[1]] > 0:
        if isNumber(e[2]):
          i += int(e[2]) - 1
        else:
          i = i - 1 + x[e[2]]
    else:
      print("Invalid instruciton!",e)
    i += 1
    #print("after",i-1,"rounds:",x['a'])
#part 2 is incomplete
def part2(lines):
  p1 = {}
  p2 = {}
  q1 = []
  q2 = []
  totalCmds = len(lines)
  print('totalCmds:',totalCmds)
  i1 = 0
  i2 = 0
  while i1 < totalCmds:
    e= lines[i].split();
    if e[1] not in p1:
      p1[e[1]]=0
    if e[1] not in p2:
      p2[e[1]]=0
   #print(e[1],':',x[e[1]])
    if e[0] == 'snd':
      if isNumber(e[1]):
        q1.append(int(e[1]))
        q2.append(int(e[1]))
      else:
        q1.append(p1[e[1]])
        q2.append(p2[e[1]])
    elif e[0] == 'set':
      if isNumber(e[2]):
        p1[e[1]] = int(e[2])
        p2[e[1]] = int(e[2])
      else:
        p1[e[1]] = x[e[2]]
        p2[e[1]] = x[e[2]]
    elif e[0] == 'add':
      if isNumber(e[2]):
        p1[e[1]] += int(e[2])
        p2[e[1]] += int(e[2])
      else:
        p1[e[1]] += p1[e[2]]
        p2[e[1]] += p2[e[2]]
    elif e[0] == 'mul':
      if isNumber(e[2]):
        p1[e[1]] *= int(e[2])
        p2[e[1]] *= int(e[2])
      else:
        p1[e[1]] *= p1[e[2]]
        p2[e[1]] *= p2[e[2]]
    elif e[0] == 'mod':
      if isNumber(e[2]):
        p1[e[1]] = p1[e[1]] % int(e[2])
        p2[e[1]] = p2[e[1]] % int(e[2])
      else:
        p1[e[1]] = p1[e[1]] % p1[e[2]]
        p2[e[1]] = p2[e[1]] % p2[e[2]]
    elif e[0] == 'rcv':
      if p1[e[1]] == 0:
        i += 1
      else:
        x[e[1]] = snd
        print(i,":",snd)
        break
    elif e[0] == 'jgz':
    #  print(e)
      if p1[e[1]] > 0:
        if isNumber(e[2]):
          i += int(e[2]) - 1
        else:
          i = i - 1 + x[e[2]]
    else:
      print("Invalid instruciton!",e)
    i += 1
    #print("after",i-1,"rounds:",x['a'])



def main():
  input_str = open('input.txt', 'r').read().strip()
  part1(input_str.splitlines())

if __name__ == "__main__":
  main()
