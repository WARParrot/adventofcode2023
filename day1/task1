numbers = []
num = str()

with open("input.txt") as f:
    file = f.readlines()

for e in file:
    for i in e:
        if i in '0123456789':
            num += str(i)
            break
    for i in range(len(e) - 1, -1, -1):
        if e[i] in '0123456789':
            num += str(e[i])
            break
    numbers.append(num)
    num = ''

numbers = list(map(int, numbers))
print(sum(numbers))
