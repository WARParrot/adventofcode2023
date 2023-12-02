numbers = []
num = str()

with open("input.txt") as f:
    file = f.read().splitlines()

for e in file:
    for i in e:
        if 'one' in e[:e.index(i)]:
            num += '1'
            break
        if 'two' in e[:e.index(i)]:
            num += '2'
            break
        if 'three' in e[:e.index(i)]:
            num += '3'
            break
        if 'four' in e[:e.index(i)]:
            num += '4'
            break
        if 'five' in e[:e.index(i)]:
            num += '5'
            break
        if 'six' in e[:e.index(i)]:
            num += '6'
            break
        if 'seven' in e[:e.index(i)]:
            num += '7'
            break
        if 'eight' in e[:e.index(i)]:
            num += '8'
            break
        if 'nine' in e[:e.index(i)]:
            num += '9'
            break
        if i in '0123456789':
            num += str(i)
            break
    for i in range(len(e) - 1, -1, -1):
        if e[i] in '0123456789':
            num += str(e[i])
            break
        if 'one' in e[i:]:
            num += '1'
            break
        if 'two' in e[i:]:
            num += '2'
            break
        if 'three' in e[i:]:
            num += '3'
            break
        if 'four' in e[i:]:
            num += '4'
            break
        if 'five' in e[i:]:
            num += '5'
            break
        if 'six' in e[i:]:
            num += '6'
            break
        if 'seven' in e[i:]:
            num += '7'
            break
        if 'eight' in e[i:]:
            num += '8'
            break
        if 'nine' in e[i:]:
            num += '9'
            break
    numbers.append(num)
    num = ''

numbers = list(map(int, numbers))
print(sum(numbers))
