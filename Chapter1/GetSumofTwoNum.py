
print('Enter the two numbers')

a = int(input('Enter a value: '))
b = int(input('Enter b value: 10'))

if a > b:
    a, b = b, a

sum = 0

for i in range(a, b+1):
    if i < b:
        print(f'{i} + ', end='')
    else:
        print(f'{i} =', end='')
    sum += i

print(f'{a} to {b} Sum is {sum}')


