# 함수 기본값
def profile(name,age,language):
    print('이름:{0}\t나이:{1}\t주 사용 언어:{2}'.format(name,age,language))
    
profile('유재석', 20 , '파이썬')
profile('김태호', 25 , '자바')

# 같은 학교 같은 학년 같은 반 수업. <== 이때 사용하는 것이 기본값

def profile(name,age=17,language='파이썬'):
    print('이름:{0}\t나이:{1}\t주 사용 언어:{2}'.format(name,age,language))

profile('유재석')
profile('김태호')

# 함수 키워드값
def profile(name,age,language):
    print(name,age,language)

profile(name='유재석',language='파이썬',age=20)
profile(language='자바',age=25,name='김태호')
