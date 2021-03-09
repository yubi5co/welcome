# 상속 
# 다중상속 : 부모가 둘 이상 
class Unit:                           # Unit: 부모
    def __init__(self,name,hp):          
        self.name = name
        self.hp = hp
        
# 공격유닛
class AttakUnit(Unit):                      # <--(Unit)상속됨, AttakUnit: 자식                       
    def __init__(self,name,hp,damage):  
        Unit.__init__(self,name,hp)        
        self.damage = damage

    def attak(self, location):
        print('{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]'.format(self.name, location, self.damage))
    
    def damaged(self,damage):
        print('{0} : {1} 데미지를 입었습니다.'.format(self.name,damage))
        self.hp -= damage
        print('{0} : 현재 체력은 {1} 입니다.'.format(self.name,self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))

#매딕: 의무병
#파이어벳 : 공격 유닛, 화염방사기.
firebat1 = AttakUnit('파이어뱃',50,16)
firebat1.attak('5시')

#공격 2번 받는다고 가정
firebat1.damaged(25)
firebat1.damaged(25) 

# 드랍쉽: 공중유닛, 수송기. 마린 / 파이어뱃 / 탱크 등을 수송. 공격 x

# 날 수 있는 기능을 가진 클래스
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self,name,location):
        print('{0}: {1} 방향으로 날아갑니다. [속도{2}]'.format(name,location,self.flying_speed))

# 공중 공격 유닛 클래스
class FlyableAttackUnit(AttakUnit, Flyable):              # <--(AttackUnit, Flyable)다중상속
    def __init__(self,name,hp,damage,flying_speed):
        AttakUnit.__init__(self,name,hp,damage)
        Flyable.__init__(self,flying_speed)

# 발키리 : 공중 공격 유닛, 한번에 14발 미사일 발사.
valkyrie = FlyableAttackUnit('발키리',200,6,5)
valkyrie.fly(valkyrie.name,'3시')

