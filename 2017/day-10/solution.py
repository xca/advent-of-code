programInput = open('input.txt', 'r').read().strip()
#programInput = open('input_example.txt', 'r').read().strip()
def reverseList(a):
    length = len(a)
    b = [0 for x in range(length)]
    for ind, item in enumerate(a):
        b[ind] = a[length - 1 - ind]
    #print(b)
    return b
def solutionPart1(inputLengths,arr,curInput,skipInput):
    #print("array is:",arr)
    arrLength= len(arr)
    #print("array length is;",len(arr))
    #inputLengths = [int(x) for x in programInput.split(',')]
    #print("input are:",inputLengths)
    length=len(inputLengths)
    curPos = curInput
    skip = skipInput
    hashlist = [x for x in range(0,listLength)]
    #print(hashlist)
    for i,step in enumerate(inputLengths):
        selected = []
        for i in range(0,step):
            index = curPos + i
            #print("before mod:",index)
            if index >= arrLength:
                index = index%arrLength
            #print("After mod:",index)
            selected.append(arr[index])
        #print("selcted is:",selected)
        reversedSelected = reverseList(selected)
        for i in range(0,step):
            index = curPos + i
            if index >= arrLength:
                index = index%arrLength
            arr[index] = reversedSelected[i]
        #print("after reversing: step is:",step,",the array is",arr)
        #this is the bug:
        curPos = curPos + (step + skip)%arrLength
        if curPos >= arrLength:
            curPos = curPos % arrLength
        skip += 1
        #print("after reversing: curpos is:",curPos,",skip is:",skip)
    #print("Part 1: the array is",arr)
    #print("Part 1:", arr[0]*arr[1])
    return curPos,skip
def sparseToDense(a):
    start = 0
    results = []
    rounds = int(len(a)/16)
    print(len(a))
    print(rounds)
    # xorsum = a[start] ^ a[start+1] ^ a[start+2] ^a[start+3]^a[start+4]^a[start+5]^a[start+6]^a[start+7]^a[start+8]^a[start+9]^a[start+10]^a[start+11]^a[start+12]^a[start+13]^a[start+14]^a[start+15]
    # print(xorsum)
    # results.append(xorsum)
    # print(results)
    for i in range(rounds):
        start = 0 + 16 * i
        xorsum = a[start] ^ a[start+1] ^ a[start+2] ^a[start+3]^a[start+4]^a[start+5]^a[start+6]^a[start+7]^a[start+8]^a[start+9]^a[start+10]^a[start+11]^a[start+12]^a[start+13]^a[start+14]^a[start+15] 
        results.append(xorsum)
        #print(results)
    #print("integer resutls:",results)
    stringResults = ['%02x' % x for x in results]
    #print("Dense result in integers is:",stringResults)
    #print("Hex dense result is:",stringResults)
    finalResult = ''.join(stringResults)
    return finalResult 

def solutionPart2(programInput,listLength,suffix):
    suffixArray = [int(x) for x in suffix.split(',')]
    arr = [x for x in range(0,listLength)]
    #print("array is:",arr)
    arrLength= len(arr)
    #print("array length is;",len(arr))
    inputLengths = [ord(x) for x in programInput] + suffixArray
    print("input are:",inputLengths)
    length=len(inputLengths)
    curPos = 0
    skip = 0
    for i in range(64):
        curPos,skip = solutionPart1(inputLengths,arr,curPos,skip)
        print("curPos",curPos)
    print("Before sparseToDense:",arr)
    final = sparseToDense(arr)
    print("Part 2:",final)
    

listLength = 256
arr = [x for x in range(0,listLength)]
#solutionPart1(programInput, arr,0,0)
suffix = "17,31,73,47,23"
solutionPart2(programInput,listLength,suffix)
# denseTest = "65 ^ 27 ^ 9 ^ 1 ^ 4 ^ 3 ^ 40 ^ 50 ^ 91 ^ 7 ^ 6 ^ 0 ^ 2 ^ 5 ^ 68 ^ 22"
# denseTestList = [int(x.strip()) for x in denseTest.split('^')]
# denseTestResult = sparseToDense(denseTestList)
# print(denseTestList)

