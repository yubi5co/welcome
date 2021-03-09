# 리스트 [] 

# 지하철 칸별로 10명, 20명, 30명
subway1 = 10
subway2 = 20
subway3 = 30

subway = [10,20,30]
print(subway)  

subway = ['유재석', '김정은', '문재인']
print(subway)

#김정은씨가 몇 번 칸에 타고 있는가?
print(subway.index('김정은'))        # index: 문자의 위치를 나타냄

#트럼프씨가 다음 정류장에서 다음 칸에 탐
subway.append('트럼프')              # append: 특정문자추가
print(subway)                       

#바이든씨를 유재석 / 김정은 사이에 태워봄
subway.insert(1,'바이든')            # insert: 특정한 위치에 넣음
print(subway)

#지하철에 있는 사람을 한 명씩 꺼냄
print(subway.pop())                 # pop(): 특정 위치의 문자 빼기
print(subway)

#같은 이름의 사람이 몇 명 있는지 확인
subway.append('유재석')
print(subway)
print(subway.count('유재석'))       # count: 출현횟수확인

#정렬도 가능 
number=[5,2,4,3,1]
number.sort()                        # sort: 순서대로 표시
print(number)

#순서 뒤집기 가능 
number.reverse()                   # reverse: 순서 뒤집기
print(number)

#모두 지우기
number.clear()                     # clear: 모두 지우기
print(number)

# 다양한 자료형 함께 사용
numlist=[5,2,4,3,1]
mixlist=['트럼프',20,'fuck']
numlist.extend(mixlist)            # extend: 리스트 확장
print(numlist)


