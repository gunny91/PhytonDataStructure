'''
클래스 만들기
클래스 선언
class Human( ):
    ''''''
인스턴스 생성
person1 = Human( )
person2 = Human( )
클래스와 인스턴스를 이용하면 데이터와 코드를 사람이 이해하기 쉽게 포장할 수 있다.
'''

class Human():
    '''Human'''

person1 = Human()
person2 = Human()

person1.language ='Korean'
person2.language ='Japanese'

print(person1.language)

print(person2.language)