'''
문자열 s의 길이가 4 혹은 6이고, 숫자로만 구성돼있는지 확인해주는 함수, solution을 완성하세요.
 예를 들어 s가 "a234"이면 False를 리턴하고 "1234"라면 True를 리턴하면 됩니다.

제한 사항
s는 길이 1 이상, 길이 8 이하인 문자열입니다.
입출력 예
s	return
"a234"	false
"1234"	true
'''
def solution(s):
    answer = True
    if (len(s) ==4 or len(s) ==6):
        for i in range(len(s)):
            if(s[i].isdigit() == False):
                return False
        return True
    else:
        return False

# def solution(s):
#     answer = True
#     if (len(s) >=4 and len(s) <=6):
#         answer =True
#     else:
#         answer = False
#     return answer


# temp = "abcdefghijklnmopqrstuvwxyz"


# print(type(temp))
#
# for i in s:
#     if(i in temp):
#         print(False)
temp = "abcdefghijklnmopqrstuvwxyz"

def solution(s):
    temp = "abcdefghijklnmopqrstuvwxyz"
    answer = True
    if (len(s) >=4 and len(s) <=6):
        if(s.isdigit() ==True):
            answer =True
        else:
                answer = False
    return print(answer)
s ="1234"
print(type(s))
solution(s)
#for i in s:


