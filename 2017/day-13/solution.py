class Layer:
  ldepth = 0
  lrange = 0
  current = 0
  down = True
  
  def __repr__(self):
    return "<Layer ldepth:%d lrange:%d current:%d down:%r>" % (self.ldepth, self.lrange, self.current, self.down)

  def go(self):
    if self.down:
        self.current += 1
    else:
        self.current -= 1 

    if self.current == 0:
        #print("switch down to True as current == 0")
        self.down = True
    if self.current == self.lrange -1:
        #print("switch down to False as current == end of lrange")
        self.down = False


def solutionPart1(lines):
    allLayers = {}
    maxDepth = 0
    for line in lines:
        d, tmp, r = line.partition(": ")
        layer = Layer()
        layer.ldepth = int(d)
        layer.lrange = int(r)
        allLayers[int(d)]=layer
        if(int(d)>maxDepth):
            maxDepth = int(d)
    # for l in allLayers:
    #     print(allLayers[l].__repr__())
    #print(maxDepth)
    severity = 0
    for i in range(maxDepth+1):
        #print("Picosecond:",i)
        if i in allLayers and allLayers[i].current == 0:
            severity += allLayers[i].ldepth * allLayers[i].lrange
        for l in allLayers:
            #print("Before go:",allLayers[l].__repr__())
            allLayers[l].go()
            #print("after go:",allLayers[l].__repr__())
    print("Part 1:",severity)

def solutionPart2(lines):
  valDict = {}
  for row in lines:
      rows = row.split(" ")
      valDict[int(rows[0][:-1])] = int(rows[-1])
  #print(valDict)

  caught = False
  for delay in range(10, 10**7):
      caught = False
      for i in valDict.keys():
          if (i+delay) % (2* valDict[i] - 2) == 0:
              caught = True
              break
      if not caught:
          print( delay)
          break

def main():
  #input_str = open('input_example.txt','r').read().strip()
  input_str = open('input.txt','r').read().strip()
  solutionPart1(input_str.splitlines())
  solutionPart2(input_str.splitlines())


if __name__ =="__main__":
  main()
