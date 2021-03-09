#super

class Unit:
    def __init__(self):
        print('Unit 생성자')

class Flyable:
    def __init__(self):
        print('Flyable 생성자')

class FlyableUnit(Unit,Flyable):    #부모 클래스를 다중상속 받을때(Unit,Flyable)는 Super를 사용하면  
    def __init__(self):             #맨처음 상속받는(Unit) 클래스에 대해서만 임의의 함수가 호출이 된다.
        super().__init__()          

# 드랍쉽
dropship = FlyableUnit()