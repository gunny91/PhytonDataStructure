try:#에러가 발생할 가능성이 있는 코드
    except Exception as ex: # 에러 종류
    # print('에러가 발생 했습니다', ex) # ex는 발생한 에러의 이름을 받아오는 변수

    try:
        a = 5
        b = 0
        c = a / b
    except Exception as c:
        print('다음과 같은 에러가 발생했습니다: {}'.format(c))