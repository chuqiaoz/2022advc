lines = []
with open('input_3.txt') as f:
    lines = [line.rstrip() for line in f]

res = 0
for i in lines:
    string1 = i[:len(i)//2]
    string2 = i[len(i)//2:]
    stringdict = dict.fromkeys(string1,0)
    for c in string2:
        if c in stringdict.keys():
            if c.islower() == True:
                res += ord(c) - 96
            else:
                res += ord(c) - 38
            break
print(str(res))



