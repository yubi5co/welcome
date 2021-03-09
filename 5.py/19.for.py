# for 반복문
#print('대기번호 : 1')
#print('대기번호 : 3')
#print('대기번호 : 4')
#       .
#       .
#       .
#       .
#print('대기번호 : 100')

#이럴떄 필요한게 반복문 for
for waitingno in range(5):                       # range(5) : 0,1,2,3,4
    print('대기번호: {}'.format(waitingno))


starbucks = ['아이언맨', '토르', '아이엠 그루트']
for customer in starbucks:
    print('{0}, 커피가 준비되었습니다.'.format(customer))
