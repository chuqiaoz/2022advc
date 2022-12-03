lines = []
with open('input_2.txt') as f:
    lines = [line.rstrip() for line in f]

res = 0
for i in lines:
    if i[2] == "X":
        res += 1
        if i[0] == 'A':
            res += 3
        elif i[0] == 'B':
            res += 0
        elif i[0] == 'C':
            res += 6
    elif i[2] == 'Y':
        res += 2
        if i[0] == 'A':
            res += 6
        elif i[0] == 'B':
            res += 3
        elif i[0] == 'C':
            res += 0
    elif i[2] == 'Z':
        res += 3
        if i[0] == 'A':
            res += 0
        elif i[0] == 'B':
            res += 6
        elif i[0] == 'C':
            res += 3

print(str(res))