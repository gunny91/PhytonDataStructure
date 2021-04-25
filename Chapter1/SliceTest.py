list1 = list(range(20))

# new_list가 5, 8, 11, 14의 값을 가지도록 list1을 slice하세요
new_list = list1[5:15:3]

print(new_list)

# reverse_list가 17, 13, 9, 5의 값을 가지도록 list1을 slice하세요
reverse_list = list1[17:4:-4]

print(reverse_list)

list1 = [0, 1, 2, 3, 4, 5]
# list1의 1부터 3까지를 slice를 이용해서 각각 11, 22, 33으로 바꿔보세요.
# 바꾸고 나면 list1은 [0, 11, 22, 33, 4, 5]가 되어야 합니다.
list1[1:4] = [11,22,33]


list2 = [0, 1, 2, 3, 4, 5]
# list2의 1부터 3까지를 del과 slice를 이용해서 지워보세요
# 바꾸고 나면 list2은 [0, 4, 5]가 되어야 합니다.
del list2[1:4]

print("list1 : {}, list2 : {}".format(list1, list2))

#Inheritance
class Car():

    def run(self):
        print("차가 달립니다.")


# 아래에서 Car를 상속받는 Truck이라는 클래스를 만들고, load라는 메소드를 만들어 보세요.
# load메소드에서는 "짐을 실었습니다."라고 출력하면 됩니다.
class Truck(Car):

    def load(self):
        print("짐을 실었습니다.")