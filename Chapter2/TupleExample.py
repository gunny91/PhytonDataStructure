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