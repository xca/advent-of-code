import re

with open('input.txt') as f:
    content = f.readlines()

fab = dict()
p = re.compile(r'\d+')
for c in content:
    nums = [int(x) for x in p.findall(c)]
    for x in range(nums[1], nums[1]+nums[3]):
        for y in range(nums[2], nums[2] + nums[4]):
            if (x, y) not in fab:
                fab[(x, y)] = 1
            else:
                fab[(x, y)] += 1
shared = 0
for k, v in fab.items():
    if v > 1:
        shared += 1
print("Part 1:", shared)

# Part 2
for c in content:
    nums = [int(x) for x in p.findall(c)]
    intact = True
    for x in range(nums[1], nums[1]+nums[3]):
        for y in range(nums[2], nums[2] + nums[4]):
            if fab[(x,y)] > 1:
                intact = False
                break
        if not intact:
            break
    if intact:
        print("Part 2:",nums[0])
        break
