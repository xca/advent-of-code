blocklist = open('input.txt', 'r').read().strip()

#blocklist = open('example_input.txt', 'r').read().strip()
blocks = [int(x) for x in blocklist.split()]
#seen = set()
seen = {}
length = len(blocks)
count1 = 0
count2 = 0
while(True):
    stringBlocks = ''.join(str(x) for x in blocks)
    if stringBlocks in seen:
        count2 = count1 - seen[stringBlocks] +1
        break
    else:
        count1+=1
        seen[stringBlocks]=count1
        #count1+=1
    maxValue = max(blocks)
    maxIndex = blocks.index(maxValue)
    #print("max value is:",maxValue,"max index is:",maxIndex)
    #print(stringBlocks)
    redisIndex = maxIndex + 1
    blocks[maxIndex] = 0
    while(maxValue > 0):
        if redisIndex >= length:
            redisIndex = 0
        blocks[redisIndex] +=1
        #print(redisIndex)
        maxValue -= 1
        redisIndex += 1
        #print(blocks)
print("Part 1:", count1)
print("Part 2:", count2)
