
def part1(steps):
    cur = 0
    buf = [0]
    for i in range(1,2018):
        forward = (steps + cur) % len(buf) 
        buf.insert(forward+1,i)
        cur = forward+1
    for i,item in enumerate(buf):
        if item == 2017:
            print("part 1:",buf[i+1])

def part2(steps):
    cur = 0
    n = 0
    for i in range(1,50000001):
        forward = (steps + cur) % i
        if forward == 0:
            n = i
        cur = forward + 1
    print("part 2:",n)

def main():
    steps = 363
    part1(steps)
    part2(steps)

if __name__ =="__main__":
  main()
