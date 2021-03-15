
print('Print + and -')
n = int(input('How many count do you want? '))

for i in range(1, n + 1):
    if i % 2:
        print('+ODD+', end='')
    else:
        print('-EVEN-', end='')

print()