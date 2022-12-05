lines = []
with open('input_4.txt') as f:
    lines = [line.rstrip() for line in f]

res  = 0
i = 0
for line in lines:
    i += 1
    l = line.split(',')
    first = l[0].split('-')
    second=l[1].split('-')
    first_first = first[0]
    first_second = first[1]
    second_first = second[0]
    second_second = second[1]
    if (int(first_first) >= int(second_first)) and (int(first_first) <= int(second_second)):
        res += 1 
    elif (int(first_second) <= int(second_second) and int(first_second) >= int(second_first)):
        res += 1
    elif (int(second_second) <= int(first_second) and int(second_second) >= int(first_first)):
        res += 1
    elif (int(second_first) >= int(first_first)) and (int(second_first) <= int(first_second)):
        res += 1 

print(str(res))
