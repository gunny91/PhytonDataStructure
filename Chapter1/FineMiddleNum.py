


print('Middle of the number')
a = int(input('enter a: '))
b = int(input('enter b: '))
c = int(input('enter c: '))

def find_middle(a, b, c):
    if a >= b:
        if b >= c:
            return b
        elif a<=c:
            return a
        else:
            return c
    elif a > c:
        return a
    elif b > c:
        return c
    else:
        return b

print(f'Middle value is {find_middle(a, b, c)}')
