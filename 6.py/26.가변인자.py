def profile(name,age,lang1,lang2,lang3,lang4,lang5):
    print('이름:{0} 나이:{1}'.format(name,age), end=' ') # end=' ' 줄바꿈 하기싫은경우 사용
    print(lang1,lang2,lang3,lang4,lang5)

profile('유재석',20,'python','java','c','c++','c#')
profile('김태호',25,'kotlin','swift','','','')

# 가변인자
def profile(name,age,*language):                      # *language를 넣고싶은만큼 넣을수 있음
    print('이름:{0} 나이:{1}'.format(name,age), end=' ')
    for lang in language:
        print(lang, end=' ')
    print()


profile('유재석',20,'python','java','c','c++','c#','html')
profile('김태호',25,'kotlin','swift')



