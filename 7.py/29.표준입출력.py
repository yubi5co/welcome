# 표준 입출력

print('python','java')
print('python','java',sep=" vs ")    # sep=: 콤마가 들어가는 부분에 입력가능

print('python','java',sep=" vs ",end='???')  #end=: 한줄로 출력하게 한다.
print('안녕하세요') 

import sys 
print('python','java',file=sys.stdout)   # stdout: 표준출력으로 처리
print('python','java',file=sys.stderr)   # stderr: 표준에러로 처리

#시험성적
scores = {'수학':0,'영어':50,'코딩':100}
for sudject,score in scores.items():
    print(sudject.ljust(8),score)         # ljust(8): 8칸의 공간을 확보하여 왼쪽으로 정렬하라는 뜻

#은행 대기순번표
# 001,002,003,004......
for num in range(1,21):
    print('대기번호 :'+ str(num).zfill(3))  # zfill(3): 3의 빈공간을 확보하여 남는공간은 0으로 채워달라는 의미


#사용자 입력을 통해서 값을 받게되면 항상 문자열 형태로 저장이된다.
answer = input('아무 값이나 입력하세요 :') 
print(type(answer))
print('입력하신 값은 ' + answer + '입니다.')