def middle_num(a, b, c):
    if( b >= a and c <= a) or (b <= a and c >= a):
        return a
    elif (a > b and c < b) or (a < b and c > b):
        return b
    return c

print('Middle of the number')
a = int(input('enter a: '))
b = int(input('enter b: '))
c = int(input('enter c: '))

print(f' get the middle is {middle_num(a, b, c)}')