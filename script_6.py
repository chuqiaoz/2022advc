with open('input_6.txt') as f:
    buffer = f.readline().rstrip()

for i in range(len(buffer)):
    marker = []
    for j in range(14):
        marker.append(buffer[i + j])
    print(marker)
    if len(marker) == len(set(marker)):
        print(marker)
        print(str(i+14))
        break
    else:
        i += 1
