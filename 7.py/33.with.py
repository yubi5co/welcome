# with: 파일을 열고 닫는 것을 좀더 편하게 작업가능

#with open('study.txt','w',encoding='utf8') as study_file:
#    study_file.write('파이썬을 열심히 공부하고 있어요')

with open('study.txt','r',encoding='utf8') as study_file:
    print(study_file.read())