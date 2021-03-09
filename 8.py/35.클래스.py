# class: 파이썬 코딩을할떄 중요함, 붕어빵 틀에 비유(틀은 하나인데 붕어빵은 무한정으로 만들수 있음.)

# 스타크레프트 테란을 예시
# 마린: 공격 유닛, 군인. 총을 쏠 수 있음
name= '마린'    # 유닛의 이름
hp= 40          # 유닛의 체력
damage= 5       #유닛 공격력

print('{}유닛이 생성되었습니다.'.format(name))
print('체력{0}, 공격력{1}\n'.format(hp,damage))

# 탱크 : 공격 유닛, 탱크, 포를 쏠 수 있는데, 일반모드 / 시즈모드.
tankname = '탱크'
tankhp = 150
tankdamage = 35

print('{}유닛이 생성되었습니다.'.format(tankname))
print('체력{0}, 공격력{1}\n'.format(tankhp,tankdamage))

# 공격하기
def attack(name,location,damage):
    print('{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2} ]'.format(name,location,damage))

attack(name,'1시',damage)
attack(tankname,'1시',tankdamage)

# 실제 게임을 하면 유닛이 많기때문에 하나하나 코딩하기 힘듬----> 클래스 사용

class Unit:
    def __init__(self,name,hp,damage):           # __init__: 파이썬에서 쓰이는 생성자
        self.name = name
        self.hp = hp
        self.damege = damage
        print("{0}유닛이 생성 되었습니다.".format(self.name))
        print('체력 {0}, 공격력 {1}'.format(self.hp,self.damege))

marine1 = Unit('마린',40,5)
marine2 = Unit('마린',40,5)
tank = Unit('탱크',150,35)

