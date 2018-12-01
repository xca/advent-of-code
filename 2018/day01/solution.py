with open('input.txt') as f:
    content = f.readlines()
content = [int(x) for x in content]
freq = 0
results = set()
results.add(freq)
found = False
while(True):
    for c in content:
        freq += c
        if freq in results:
            print(freq)
            found = True
            break
        else:
            results.add(freq)
    if found:
        break
# print(freq)
