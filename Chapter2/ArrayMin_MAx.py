from typing import Sequence, Any

a =[1, 2, 3, 44, 55, 60]

#tempMax = a[0]

#if a[1] > tempMax: tempMax =a[1]

#MaxOF
def max_of(a: Sequence) -> Any:
    tempMax = a[0]
    for i in range(1, len(a)):
        if a[i] > tempMax:
            tempMax = a[i]
    return tempMax


print('Get the max number')
num = int(input('Enter the elements'))
x = [None] * num

for i in range(num):
    x[i] = int(input(f'x[{i}] enter...'))

print(f'max of {max_of(x)}')

