from collections import defaultdict

def part1():
    programInput = open('input.txt','r').read().strip()
    lines = list(programInput.splitlines()) 
    matrix = [list(l) for l in lines]
    # defind a grid as dictionary and set default value as "."
    grid = defaultdict(lambda:".")
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            grid[i,j] = lines[i][j]
    # initial position x and y
    y = len(lines[0])//2
    x = len(lines)//2
    U,L,D,R = 0,1,2,3
    d = U
    i = 0
    infected = 0
    while i < 10000:
        i += 1
        if grid[x,y] == '.':
            d = (d + 1) % 4
            grid[x,y] = '#'
            infected += 1
        elif grid[x,y] == '#':
            d = (d + 3) % 4
            grid[x,y] = '.'
        if d == U:
            x-=1
        elif d == D:
            x+=1
        elif d == L:
            y-=1
        elif d == R:
            y+= 1
        else:
            print("Wrong dirction:",d)
    print("Part 1:",infected)
    return infected

def part2():
    programInput = open('input.txt','r').read().strip()
    lines = list(programInput.splitlines()) 
    matrix = [list(l) for l in lines]
    grid = defaultdict(lambda:".")
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            grid[i,j] = lines[i][j]
    # initial position x and y
    y = len(lines[0])//2
    x = len(lines)//2
    U,L,D,R = 0,1,2,3
    d = U
    i = 0
    infected = 0
    while i < 10000000:
        i += 1
        if grid[x,y] == '.':
            d = (d + 1) % 4
            grid[x,y] = 'W'
        elif grid[x,y] == '#':
            d = (d + 3) % 4
            grid[x,y] = 'F'
        elif grid[x,y] == 'W':
            grid[x,y] = '#'
            infected += 1
        elif grid[x,y] == 'F':
            grid[x,y] = '.'
            d = (d+2)%4
        else:
            print("grid",x,y,"has an invalid state",grid[x][y])
        
        if d == U:
            x-=1
        elif d == D:
            x+=1
        elif d == L:
            y-=1
        elif d == R:
            y+= 1
        else:
            print("Wrong dirction:",d)
    print("Part 2:",infected)
    return infected

def main():
    part1()
    part2()

if __name__ == "__main__":
    main()