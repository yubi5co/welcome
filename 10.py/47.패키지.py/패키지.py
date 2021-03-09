# 패키지 : 모듈들을 모아놓은 집합

#import travel.thailand
#trip_to = travel.thailand.Thailandpackage()
#trip_to.detail()

#from travel.thailand import Thailandpackage
#trip_to = Thailandpackage()
#trip_to.detail

#from travel import vietnam
#trip_to = vietnam.Vietnampakage()
#trip_to.detail()

from travel import *
#trip_to = vietnam.Vietnampakage()
trip_to = thailand.Thailandpackage()
trip_to.detail()

# 패키지 모듈위치 (위치파악)
import inspect           
import random
print(inspect.getfile(random))
print(inspect.getfile(thailand))


