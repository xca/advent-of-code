class Node:
  name = ''
  children = []

  def __repr__(self):
    return "<Node name:%s children:%s>" % (self.name, self.children)

  def directChildren(self):
    return self.children

def solution(lines):
  allNodes = {}
  for line in lines:
    splitted = line.split('<->')
    n = Node()
    n.name = splitted[0].strip()
    n.children = [x.strip() for x in splitted[1].split(',')]
    allNodes[n.name]=n
  visited = set(['0'])
  # visted 0's children and add them to visited
  connected = allNodes['0'].directChildren()
  count = 1
  while(len(connected)>0):
    count += 1
    nodeName = connected.pop()
    visited.add(nodeName)
    for x in allNodes[nodeName].children:
      if x not in visited:
        connected.append(x)
        visited.add(x)
  print("Part 1:",count)
  isolated = set()
  for x in allNodes.keys():
    if x in visited:
      continue
    else:
      isolated.add(x)
  group = 1
  for k in isolated:
    if k in visited:
      continue
    else:
      group += 1
      connected = allNodes[k].children
      visited.add(k)
      while(len(connected)>0):
        nodeName = connected.pop()
        visited.add(nodeName)
        for x in allNodes[nodeName].children:
          if x not in visited:# and x != nodeName:
            connected.append(x)
            visited.add(x)
  print("Part 2:",group)

def main():
  #input_str = open('input_example.txt','r').read().strip()
  input_str = open('input.txt','r').read().strip()
  solution(input_str.splitlines())


if __name__ =="__main__":
  main()
