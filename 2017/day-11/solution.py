directionString = open('input_notepad.txt','r').read().strip()
#directionString = "se,sw,se,sw,sw"
directions = directionString.split(',')

def cancel(count):
  #2 steps -> 0 steps:
  minNS = min(count['n'],count['s'])
  count['n'] -= minNS
  count['s'] -= minNS

  minNeSw = min(count['ne'],count['sw'])
  count['ne'] -= minNeSw
  count['sw'] -= minNeSw

  minNwSe = min(count['nw'], count['se'])
  count['nw'] -= minNwSe
  count['se'] -= minNwSe

def reduce(count):
# N + SW = NW
  minNSw = min(count['n'],count['sw'])
  count['n'] -= minNSw
  count['sw'] -= minNSw
  count['nw'] += minNSw
# N + SE = NE
  minNSe = min(count['n'],count['se'])
  count['n'] -= minNSe
  count['se'] -= minNSe
  count['ne'] += minNSe
# S + NW = SW
  minSNw = min(count['s'],count['nw'])
  count['s'] -= minSNw
  count['nw'] -= minSNw
  count['sw'] += minSNw
# S + NE = SE
  minSNe = min(count['s'],count['ne'])
  count['s'] -= minSNe
  count['ne'] -= minSNe
  count['se'] += minSNe
# NW + NE = N
  minNwNe = min(count['nw'],count['ne'])
  count['nw'] -= minNwNe
  count['ne'] -= minNwNe
  count['n'] += minNwNe
# SW + SE = S
  minSwSe = min(count['sw'],count['se'])
  count['sw'] -= minSwSe
  count['se'] -= minSwSe
  count['s'] += minSwSe

count = {'n':0,'s':0,'e':0,'w':0,'ne':0,'nw':0,'se':0,'sw':0}

maxDist = 0
s = 0
for d in directions:
    if d in count:
      count[d] += 1
    else:
      print("Invalid input:",d)
    cancel(count)
    reduce(count)
    s = 0
    for key,val in count.items():
      s += val
    if s > maxDist:
      maxDist = s
print("Final array:",count)
print("final steps are:",s)
print("max dist is:",maxDist)
