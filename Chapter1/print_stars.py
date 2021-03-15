
print('Print * star')

n = int(input('How many lines do you want to print? '))
w = int(input('How many lines do you want to change? '))

for i in range(n):
    print('*', end='')
    if i % w == w - 1:
        print()

if n % w:
    print()