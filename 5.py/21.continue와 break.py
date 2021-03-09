# continue 와 break 

# 2,5번 학생은 결석, 다른 학생에게 책을 읽히는 경우
absent = [2,5] #결석
nobook = [7] #책을 깜빡했음
for student in range(1,11): # 1,2,3,4,5,6,7,8,9,10
    if student in absent:
        continue             # continue 아래있는 문장을 더이상 실행시키지 않고, 다음 반복으로 진행하라는 명령어
    elif student in nobook:
        print('오늘 수업 여기까지. {0}는 교무실로 따라와'.format(student))
        break                # break 뒤에 반복문이 있든없든 반복문을 탈출함
    print('{0}, 책을 읽어봐'.format(student))
