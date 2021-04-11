'''
    List의 다양한 기능
    List의 기능
    list.index( value ) : 값을 이용하여 위치를 찾는 기능
    list.extend( [value1, value2] ) : 리스트 뒤에 값을 추가
    list.insert( index, value ) : 원하는 위치에 값을 추가
    list.sort( ) : 값을 순서대로 정렬
    list.reverse( ) : 값을 역순으로 정렬
'''
def safe_index(my_list, value):
    # 함수를 완성하세요
    if value in my_list:
        return my_list.index(value)

    else:
        return None

print(safe_index([1,2,3,4,5], 5))
print(safe_index([1,2,3], 5))

'''
insert(), sort(), reverse()를 사용해서 다음 코드에 주석으로 적힌 내용을 만들어 보세요.

문제를 해결하기 위해 리스트의 기능에 대해 알아보아요.

list.insert(index, value) : 원하는 위치에 값을 추가합니다
list = [1, 2, 3]
list.insert(3, 4)     #list = [1, 2, 3, 4]로 4가 추가되었습니다.
list.sort() : 값을 순서대로 정렬
list = [3, 5, 6, 4, 2, 1]
list.sort()           #list = [1, 2, 3, 4, 5, 6]으로 정렬됩니다.
list.reverse() : 값을 역순으로 정렬
list = [3, 5, 6, 4, 2, 1]
list.reverse()     #list = [1, 2, 4, 6, 5, 3] 역순으로 정렬
'''

list1 = [1, 2, 3, 4]

# 아래줄에서 list1의 1번째 자리에 8을 넣고 원래 있던 값은 오른쪽으로 밀어 보세요.
list1.insert(0,8)

print("첫 번째 자리에 8을 넣은 결과 : {}".format(list1))
# 아래줄에서 list1을 작은 수부터 큰 수로 정렬해 보세요
list1.sort()

print("list1을 작은 수부터 큰 수로 정렬한 결과 : {}".format(list1))
# 아래줄에서 list1을 거꾸로 만들어 보세요
list1.reverse()

print("list1을 거꾸로 정렬한 결과 : {}".format(list1))

'''
List와 문자열
List와 String
리스트와 문자열은 유사하다.
서로 변환이 가능하다.
list = str.split( ) : 문자열에서 리스트로
" ".join( list ) : 리스트에서 문자열으로
'''
'''
List와 String의 유사성을 이용해 보세요.
리스트와 문자열은 서로 변환할 수 있습니다.

예를 들어,

str = "10:35:27"
list = str.split(":")             #문자열을 ":"기준으로 리스트화
new_str = ":".join(list)          #리스트를 ":"기준으로 문자열화
이처럼 ":"을 기준으로 문자열과 리스트를 서로 변환 할 수 있습니다.
'''
str = "오늘은 날씨가 흐림"

# split()을 이용해서 str을 공백으로 나눈 문자열을 words에 저장하세요
words = str.split()


# index()를 이용해서 "흐림"이 words의 몇번째에 있는지 찾고,
# position에 저장하세요.
position = words.index('흐림')


words[position] = "맑음"

# join()을 이용해서 words를 다시 문자열로 바꿔 new_str에 저장하세요.
# words를 문자열로 바꿀때는 공백 한 칸을 기준으로 붙이면 됩니다.
new_str = " ".join(words)
print(new_str)