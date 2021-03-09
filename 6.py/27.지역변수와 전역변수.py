# 지역변수와 전역변수
# 지역변수: 함수(박스)내에서만 사용가능, 전역변수: 모든공간에서 사용가능

gun=10

def chekpoint(soldiers): #경계근무
    global gun # 전역 공간에 있는 gun 사용
    gun = gun-soldiers
    print('[함수 내] 남은 총: {0}'.format(gun))

def chekpoint_ret(gun, soliders):
    gun = gun-soliders
    print('[함수 내] 남은 총: {0}'.format(gun))
    return gun

print('전체 총: {0}'.format(gun))
#chekpoint(2) # 2명이 경계근무나감
gun = chekpoint_ret(gun,2)
print('남은 총: {0}'.format(gun))