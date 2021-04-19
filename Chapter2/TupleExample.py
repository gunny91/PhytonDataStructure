tuple1 = (1,2,3)
tuple2 = 1,2,3
list3 = [1,2,3]
tuple3 = tuple(list3)

if tuple1 == tuple2 == tuple3:
    print("tuple1과 tuple2와 tuple3은 모두 같습니다.")

    tuple1 = (11, 22, 33)
    for i in range(len(tuple1)):
        print(tuple1[i])


x = 3
y = 5

position = x,y

print("x, y로 이루어진 튜플 position의 값은 {}입니다.".format(position))

a, b = 1, 2
c = a, b      #c = (1, 2)

c = (3, 4)
d, e = c     # c의 값을 언패킹하여 d, e에 값을 저장
f = d, e     # 변수 d와 e를 f에 패킹

a = 1
b = 2

#코드를 작성해 보세요. 위치 교환
a, b = b,a


print("a : {}, b : {}".format(a, b))

for a in enumerate(list):
    print('{}번째 값: {}'.format(a[0], a[1]))

for a in enumerate(list):
    print('{}번째 값: {}'.format(*a))

    for a in dict.items():
        print('{}의 나이는:{}'.format(a[0], a[1]))

    for a in dict.items():
        print('{}의 나이는:{}'.format(*a))

ages = {'Tod' : 35, 'Jane' : 23, 'Paul' : 62}

for a in ages.items():
    print('{}의 나이는:{}'.format(a[0], a[1]))

for a in ages.items():
    print('{}의 나이는:{}'.format(*a))    # 두 출력 결과가 같습니다.