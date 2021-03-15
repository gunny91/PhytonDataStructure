

print('Print stars')

n = int(input('Print how many counts? '))
w = int(input('How many lines do you want to change? '))

for _ in range(n // w):
    print('*' * w)

rest = n % w
if rest:
    print('*' * rest)