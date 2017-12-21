import string

inp = open("input.txt",'r').read()
lines = list(inp.splitlines())

matrix = [list(l) for l in lines]
totalColumns = len(matrix[0])
totalRows = len(lines)
x,y = 0,0
while matrix[0][y] != '|':
    y+=1

D,U,L,R = 1,2,3,4
d = D
letters = []
steps = 0
while True:
    if matrix[x][y] == '|' or matrix[x][y]=='-':
        if d == D:
            x+=1
        elif d == U:
            x-=1
        elif d == R:
            y+=1
        elif d == L:
            y-=1
    elif matrix[x][y] == '+': 
        if d in [U,D]:
            if y+1 < totalColumns and matrix[x][y+1] != ' ':
                d = R
                y=y+1
            else:
                d = L
                y=y-1
        elif d in [L,R]:
            if x+1 < totalRows  and matrix[x+1][y] != ' ':
                d = D
                x += 1
            else:
                d = U
                x-= 1
    elif matrix[x][y] in string.ascii_uppercase:
        letters.append(matrix[x][y])
        if d == D:
            x+=1
        elif d == U:
            x-=1
        elif d == R:
            y+=1
        elif d == L:
            y-=1
    else:
        break
    steps += 1
print("Part 1:",''.join(letters))
print("Part 2:",steps)