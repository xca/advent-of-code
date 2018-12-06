def collapse(slist):
    i = 0
    while i < len(slist)-1:
        if abs(ord(slist[i])-ord(slist[i+1])) == 32:
            del(slist[i:i+2])
            if i!=0:
                i -=1
        else:
            i+= 1
    return len(slist)

with open('input.txt') as f:
    line = f.readline()
letters = list(line)
print("Part 1:", collapse(letters))
#part 2
alphas = 'abcdefghijklmnopqrstuvwxyz'
minLen = len(letters)
for c in alphas:
    rest = [x for x in letters if x!=c and x!=c.upper()]
    minLen = min(collapse(rest), minLen)
print("Part 2:",minLen)
