
print('Print + and -')
n = int(input('How mnay? '))

for i in range(n // 2):
    print('+-', end='')

if i % 2:
    print('+', end='')

print()