lines = []
with open('input_2.txt') as f:
    lines = [line.rstrip() for line in f]

res = 0
for i in lines:
    if i[2] == "X": # lose 0
        res += 0
        if i[0] == 'A':
            res += 3
        elif i[0] == 'B':
            res += 1
        elif i[0] == 'C':
            res += 2
    elif i[2] == 'Y': # draw 3
        res += 3
        if i[0] == 'A':
            res += 1
        elif i[0] == 'B':
            res += 2
        elif i[0] == 'C':
            res += 3
    elif i[2] == 'Z': # win 6
        res += 6
        if i[0] == 'A':
            res += 2
        elif i[0] == 'B':
            res += 3
        elif i[0] == 'C':
            res += 1

print(str(res))