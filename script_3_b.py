lines = []
with open('input_3.txt') as f:
    lines = [line.rstrip() for line in f]

res = 0
counter = 0
i = 0
while i in range(len(lines)-2):
    first = lines[i]
    second = lines[i + 1]
    third = lines[i + 2]
    i += 3
    new = []
    stringdict = dict.fromkeys(first,0)
    for c in second:
        if c in stringdict.keys():
            new.append(c)
    newdict = dict.fromkeys(new,0)
    for c in third:
        if c in newdict.keys():
            counter += 1
            if c.islower() == True:
                res += ord(c) - 96
            else:
                res += ord(c) - 38
            break
    
print(str(res))
