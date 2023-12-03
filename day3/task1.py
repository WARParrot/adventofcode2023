numbers = []
adjacent = False
number = str()

with open("input.txt") as f:
    file = f.read().splitlines()

for i in range(len(file)):
    if adjacent:
        numbers.append(int(number))
        adjacent = False
    number = ''
    for e in range(len(file[i])):
        if file[i][e] in '0123456789':
            number += file[i][e]
            if file[i][max(0, e-1)] not in '.0123456789' \
                    or file[i][min(len(file[i])-1, e+1)] not in '.0123456789' \
                    or file[max(0, i-1)][e] not in '.0123456789' \
                    or file[max(0, i-1)][max(0, e-1)] not in '.0123456789' \
                    or file[max(0, i-1)][min(len(file[i])-1, e+1)] not in '.0123456789' \
                    or file[min(len(file[i])-1, i+1)][e] not in '.0123456789' \
                    or file[min(len(file[i])-1, i+1)][max(0, e-1)] not in '.0123456789' \
                    or file[min(len(file[i])-1, i+1)][min(len(file[i])-1, e+1)] not in '.0123456789':
                adjacent = True
        else:
            if adjacent:
                numbers.append(int(number))
                adjacent = False
            number = ''

print(sum(numbers))
