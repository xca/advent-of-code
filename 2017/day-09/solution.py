programsInput = open('input.txt', 'r').read().strip()

testdata = "{}"
testdata2 = "{{<!!>},{<!!>},{<!!>},{<!!>}}"
#testdata3 = "{{<a!>},{<a!>},{<a!>},{<ab>}}"
testdata3 = '<{o"i!a,<{i<a>'
testdata4 = '<{!>}>'

def countGarbage(data):
    score = 0

    scores = []
    notFlag = False
    garbage = False

    scores.append(0)

    gcount = 0
    gtotal = 0

    for c in data:
        if notFlag:
            notFlag = False
            continue
        if garbage:
            if c == '>':
                gtotal += gcount
                garbage = False
                continue
            elif c == '!':
                notFlag = True
                continue
            else:
                gcount += 1
        else:
            if c == "{":
                scores.append(scores[-1]+1)
            elif c == "}":
                score += scores.pop()
            elif c == "<":
                garbage = True
                gcount = 0
                continue
            elif c == ",":
                continue
            else:
                continue
    print("Part 1:",score)
    print("Pare 2:", gtotal)

countGarbage(programsInput)
#countGarbage(testdata4)

