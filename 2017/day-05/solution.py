jumpList = open('input.txt', 'r').read().strip()

jumps = [int(x.strip()) for x in jumpList.splitlines() if x.strip() != '']

i = 0
length = len(jumps)

count = 0
while(i>=0 and i<length):
  count += 1
  steps = jumps[i]
  jumps[i] += 1
  i =i + steps
  
print("Part 1:",count)

i = 0
jumps = [int(x.strip()) for x in jumpList.splitlines() if x.strip() != '']
count2 = 0
while(i>=0 and i<length):
  count2 += 1
  steps = jumps[i]
  if steps >= 3:
    jumps[i] -= 1
  else:
    jumps[i] +=1
  i = i + steps
print("Part 2:", count2)
