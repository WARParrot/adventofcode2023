IDs = int()

with open("input.txt") as f:
    file = f.read().splitlines()

for i in file:
    ID = int(i.split(':')[0].split()[1])
    i = i.split(':')[1]
    bad = False

    for e in i.split('; '):
        red, green, blue = 0, 0, 0
        for k in e.split(', '):
            h = k.split()
            if h[1] == 'red':
                red += int(h[0])
            elif h[1] == 'green':
                green += int(h[0])
            elif h[1] == 'blue':
                blue += int(h[0])
        if red > 12 or green > 13 or blue > 14:
            bad = True
    if not bad:
        IDs += ID

print(IDs)
