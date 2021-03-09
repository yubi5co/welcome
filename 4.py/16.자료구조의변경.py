# 자료구조의변경
#커피숍
menu = {'커피','우유','주스'}   #set형식 {}
print(menu,type(menu))

menu = list(menu)              #list형식 [] 
print(menu, type(menu))

menu = tuple(menu)             #tuple형식 <> 
print(menu,type(menu))

menu = set(menu)               #set형식{} 
print(menu,type(menu))