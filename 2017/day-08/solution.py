programsInput = open('input.txt', 'r').read().strip()
#programsInput = open('input_example.txt', 'r').read().strip()

registers = {}
maxRegister = 0
for instruction in programsInput.splitlines():
    instructions = instruction.split()
    if instructions[0] not in registers:
        registers[instructions[0]] = 0
    if instructions[4] not in registers:
        registers[instructions[4]] = 0
    satisfy = False
    if instructions[5] == ">":
        if registers[instructions[4]] > int(instructions[6]):
            satisfy = True
    if instructions[5] == "<":
        if registers[instructions[4]] < int(instructions[6]):
            satisfy = True
    if instructions[5] == ">=":
        if registers[instructions[4]] >= int(instructions[6]):
            satisfy = True
    if instructions[5] == "<=":
        if registers[instructions[4]] <= int(instructions[6]):
            satisfy = True
    if instructions[5] == "==":
        if registers[instructions[4]] == int(instructions[6]):
            satisfy = True
    if instructions[5] == "!=":
        if registers[instructions[4]] != int(instructions[6]):
            satisfy = True
    if satisfy:
        if instructions[1] == 'inc':
            registers[instructions[0]] += int(instructions[2])
        elif instructions[1] == 'dec':
            registers[instructions[0]] -= int(instructions[2])
    if registers[instructions[0]] > maxRegister:
        maxRegister = registers[instructions[0]]
max = 0
for key in registers:
    if registers[key] > max:
        max = registers[key]
print("part 1:",max)
print("Part 2:",maxRegister)