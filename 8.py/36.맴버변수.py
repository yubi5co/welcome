# 멤버변수 : 클래스 내에서 정의된 변수

class Unit:
    def __init__(self,name,hp,damage):          
        self.name = name
        self.hp = hp
        self.damege = damage
        print("{0}유닛이 생성 되었습니다.".format(self.name))
        print('체력 {0}, 공격력 {1}'.format(self.hp,self.damege))

#marine1 = Unit('마린',40,5)
#marine2 = Unit('마린',40,5)
#tank = Unit('탱크',150,35)

# 레이스 : 공중유닛, 비행기. 클로킹(상대방에게 보이지 않음)
wraith1 = Unit('레이스',80,5)
print('유닛이름: {0}, 공격력 : {1}'.format(wraith1.name, wraith1.damege))

# 클로킹: 프로토스 아칸의 마인드 컨트롤(상대방 유닛을 내 것으로 만드는 것)
wraith2 = Unit('빼앗은 레이스', 80 ,5)
wraith2.clocking = True

if wraith2.clocking == True:
    print("{0}는 현재 클로킹 상태입니다.".format(wraith2.name))

