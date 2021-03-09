# 사전

#목욕탕에 사물함의 열쇠번호와 사용자가 있다면??
cabinet = {3:'유재석', 100:'김태호'}  # 열쇠는 3이고 그 열쇠는 유재석이 쓰고 있다는 의미
print(cabinet[3])                    # 3번 열쇠에는 유재석의 짐이 들어가 있다
print(cabinet[100])
print(cabinet.get(3))                # cabinet[3]과 같은 의미 (대신에 오류가 발생x)

print(3 in cabinet) # true 로 출력
print(5 in cabinet) # false 로 출력

#새 손님
print(cabinet)
cabinet[3] = '바이든'
cabinet[50] = '트럼프'
print(cabinet)

#간 손님
del cabinet[3]   # del로 제거
print(cabinet)

# 총 사용중인 key 들만 출력
print(cabinet.keys())      #key

# value(사용자)들만 출력
print(cabinet.values())    #value

# key,value 쌍으로 출력
print(cabinet.items())     #items

#목욕탕 폐점
cabinet.clear              #clear
print(cabinet)