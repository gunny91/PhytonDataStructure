list1 = []
list2 = [1, 2, 3]
list3 = ['A', 'B', 'C']

list4 = list()
list5 = list('ABC')
list6 = list([1, 2, 3])
list7 = list((1, 2, 3))
list8 = list({1, 2, 3})

list9 = list(range(7))
list10 = list(range(3,8))
list11 = list(range(3,13,2))
list12 = [None] * 5

print(list11)
print(list12)

tuple01 =()
tuple2 =1,
tuple3 = (1,)
print(tuple01)
x = [1, 2, 3]
a, b, c = x
print(a, b, c)

print('Slice way')
s=[1,2,3,4,5,6,7]
print(s[0:6])
print(s[0:7:2]) # Print with odd numbers

a,b,c =1,2,3
print(a,b,c)

x =6
y =2
x, y = y+2, x+3

print(x,y)

n =12
print(id(n))
x= 0
print(type(x+17))
#print(type(x=17))
print(len(s))