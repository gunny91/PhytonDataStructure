temp = ['r', 'a', 'c', 'e', 'a', 'c', 'a', 'r']
# "A man, a plan, a canal: Panama"

# def isPalindrome(self, s: str) -> bool:
#     strs = []
#     for char in s:
#         if char.isalnum():
#             strs.append(char.lower())
#     print(strs)
#     while len(strs) >1 :
#         if strs.pop(0) != strs.pop():
#             return False
#     return True
#
# isPalindrome(temp)

strs = temp
for char in strs:
    if char.isalnum():
        strs.append(char.lower())
    print(strs)