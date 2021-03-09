# 예외처리: 에러가 발생했을때 그에 대한 처리를 해주는것 try,exept
try:

    print('나누기 전용 계산기입니다.')
    num1 = int(input('첫번째 숫자를 입력하세요 : '))
    num2 = int(input('두번째 숫자를 입력하세요 : '))
    print('{0}/{1} = {2}'.format(num1, num2, int(num1/num2)))

except ValueError:
    print('에러! 잘못된 값을 입력하였습니다.')
