lines = []
with open('input_5.txt') as f:
    lines = [line.rstrip() for line in f]

stacks = [['F','R','W'],
['P','W','V','D','C','M','H','T'],
['L','N','Z','M','P'],
['R','H','C','J'],
['B','T','Q','H',"G",'P','C'],
['Z',"F",'L','W',"C",'G'],
['C','G','J','Z','Q','L','V','W'],
['C','V','T','W','F','R','N','P'],
['V','S','R','G','H','W','J']]

for s in stacks:
    s = s.reverse()


for line in lines:
    instruction = [int(s) for s in line.split() if s.isdigit()]
    begin = instruction[1] - 1
    desti = instruction[2] - 1
    amount = instruction[0]
    offset = stacks[begin][len(stacks[begin]) - amount:]
    stacks[begin] = stacks[begin][:len(stacks[begin]) - amount]
    stacks[desti] = stacks[desti] + offset
print(stacks)