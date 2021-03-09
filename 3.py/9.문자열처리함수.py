#문자열처리함수
python = 'Python is Amazing'
print(python.lower())  # .lower:소문자로출력
print(python.upper())  # .upper:대문자로출력
print(python[0].isupper()) #첫번째 글자가 대문자인가 알려줌
print(len(python)) #문자열 전체길이를 반환해줌
print(python.replace('Python','java')) #Python이라는 문자를 찾아서 java로 변환

index = python.index('n')  #index:어떤 문자가 어느위치에 있는지 확인
print(index)
index = python.index('n', index +1) #두번째 n을 찾기위해 index(첫번째n) +1을 적용
print(index)

print(python.find('java')) #문자열에는 java가 없으니까 -1로 나타난다
#print(python.index('java')) 로 할경우 오류가생겨 다음문자 출력안됨

print(python.count('n')) #count: 문자열에 n이 총 몇번 등장하는지 알려줌