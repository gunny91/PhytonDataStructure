

def solution(n):
    answer = []
    answer = n.reverse()
    print(answer)
    return answer

n = 12345
temp =[n]

for i in range(len(temp)):
    print(temp[i])
    print(temp.reverse())

#solution(n)