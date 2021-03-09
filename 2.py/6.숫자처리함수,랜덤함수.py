#숫자처리함수
print(abs(-5))           # ads:절대값 5 
print(pow(4,2))         #4^2 = 4*4 =16
print(max(5,2,7))       # max:최대값 찾아줌 7 
print(min(5,2,7))        # min:최소값 찾아줌 2
print(round(3.14))       # round:반올림 3
print(round(4.99))         # round:반올림 5
print('-------------------------------')
#랜덤함수
from random import *          # 나중에 배움

print(random())               # 0.0~1.0 미만의 임의의(랜덤) 값 생성
print(random()*10)             # 0.0~10.0 미만의 임의의 값 생성
print(int(random()*10))          #소수점이 보기싫은경우 int삽입
print(int(random()*10)+1)        #1~10 이하의 임의의 값 생성 (0을 제거 하고싶은 경우)

print(randrange(1,46))           # 1~46 미만의 임의의 값 생성
print(randint(1,45))           # 숫자 양쪽 끝값모두 포함 1~45이하의 임의의 값 생성


