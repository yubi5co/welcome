# 튜플

menu = ('돈까스','치즈까스')
print(menu[0])
print(menu[1])

name = '트럼프'
age = 20
hobby = '코딩'
print(name,age,hobby)

# 튜플을 이용하면
(name,age,hobby) = '바이든', 20, '코딩'
print(name,age,hobby)

# 집합 (set)  {}

myset={1,2,3,3,3}    # 중복이 안됨, 순서 없음
print(myset)

java={'유재석','김태호','박명수'}
python=set(['유재석','트럼프'])

#교집합 출력 (java 와 python을 모두 할 수 있는 개발자)
print(java & python)                   #방법1 &
print(java.intersection(python))       #방법2 intersection

#합집합 출력 (java 도 할수있거나 python도 할수있는 개발자)
print(java | python)                   #방법1 |
print(java.union(python))              #방법2 union

#차집합 출력 (java는 할 수 있지만 python은 할 줄 모르는 개발자)
print(java - python)                   #방법1 -
print(java.difference(python))         #방법2 difference

# python 할 줄 아는 사람이 늘어남
python.add('김태호')                   # add
print(python) 

# java를 잊었어요 
java.remove('김태호')
print(java)                           #remove

