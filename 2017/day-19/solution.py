import string

inp = open("input.txt",'r').read()
lines = list(inp.splitlines())

matrix = [list(l) for l in lines]
totalColumns = len(matrix[0])
totalRows = len(lines)
# print(matrix[5])
# print("row length:",totalRows)
# print("column length:",totalColumns)
x,y = 0,0
while matrix[0][y] != '|':
    y+=1

D,U,L,R = 1,2,3,4
d = D
letters = []
steps = 0
while True:
    # print(x,y,matrix[x][y])
    if matrix[x][y] == '|':
        if d == D:
            x+=1
        elif d == U:
            x-=1
        elif d == R:
            y+=1
        elif d == L:
            y-=1
        steps += 1
    elif matrix[x][y] == '-':
        if d == D:
            x+=1
        elif d == U:
            x-=1
        elif d == R:
            y+=1
        elif d == L:
            y-=1
        steps += 1
    elif matrix[x][y] == '+': 
        if d in [U,D]:
            if y+1 < totalColumns and matrix[x][y+1] != ' ':
                d = R
                y=y+1
            else:
                d = L
                y=y-1
        elif d in [L,R]:
            # print(x,y)
            # print(matrix[x][y])
            # print(matrix[x+1][y])
            if x+1 < totalRows  and matrix[x+1][y] != ' ':
                d = D
                x += 1
            else:
                d = U
                x-= 1
        steps += 1
    elif matrix[x][y] in string.ascii_uppercase:
        # print(matrix[x][y])
        letters.append(matrix[x][y])
        if d == D:
            x+=1
        elif d == U:
            x-=1
        elif d == R:
            y+=1
        elif d == L:
            y-=1
        steps += 1
    else:
        break
print("Part 1:",''.join(letters))
print("Part 2:",steps)