IDs = int()

with open("input.txt") as f:
    file = f.read().splitlines()

for i in file:
    ID = int(i.split(':')[0].split()[1])
    i = i.split(':')[1]
    red, green, blue = 0, 0, 0

    for e in i.split('; '):
        for k in e.split(', '):
            h = k.split()
            if h[1] == 'red' and int(h[0]) > red:
                red = int(h[0])
            elif h[1] == 'green' and int(h[0]) > green:
                green = int(h[0])
            elif h[1] == 'blue' and int(h[0]) > blue:
                blue = int(h[0])
    IDs += red * green * blue


print(IDs)
