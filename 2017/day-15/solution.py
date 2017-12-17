def nextValue(prev,factor):
    div = 2147483647
    nextVal = (prev * factor) % div
    return nextVal
def int2bin16digits(i):
    print(i)
    if i == 0:
        return "0"
    s = ''
    while i:
        if i & 1 == 1:
            s = "1" + s
        else:
            s = "0" + s
        i = int(i/2)
        if len(s) == 16:
            break
    return s
def solution():
    p1 = 65
    p2 = 8921
    f1 = 16807
    f2 = 48271
    for i in range(5):
        p1 = nextValue(p1,f1)
        p2 = nextValue(p2,f2)
        #print(p1,p2)
        b1 = int2bin16digits(p1)
        b2 = int2bin16digits(p2)
        print(b1,b2)

def main():
    solution()

if __name__ =="__main__":
  main()
