# pass

class Unit:                           
    def __init__(self,name,hp):          
        self.name = name
        self.hp = hp

# 건물
class BuildingUnit(Unit):
    def __init__(self,name,hp,location):
        pass                                 # Pass: 아무것도 안하고 일단은 넘아간다는 의미
#서플라이 디폿 : 건물, 1개 건물 = 8유닛.
supply_depot = BuildingUnit('서플라이 디폿',500,'7시')

def game_start():
    print('[알림] 새로운 게임을 시작합니다.')

def game_over():
    pass

game_start()
game_over()