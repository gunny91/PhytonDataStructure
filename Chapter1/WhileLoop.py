
print('Get the sum from 1 to nth numbers')
temp = int(input('Enter the nth number: '))

sum = 0
i = 1

while i <= temp:
    sum += i
    i += 1

print(f'The sum is {sum}')