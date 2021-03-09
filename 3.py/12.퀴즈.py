#퀴즈) 사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오

#예) http://naver.com
#규칙1 : http:// 부분은 제외 ==>naver.com
#규칙2 : 처음만나는점(.) 이후 부분은 제외 ==>naver
#규칙3 : 남은 글자 중 처음 세자리 + 글자갯수 + 글자 내 'e' 갯수 + '!'로 구성
#                 (nav)             (5)           (1)            (!)

#예) 생성된 비밀번호 :nav51!    

url='http://naver.com'
mystr=url.replace('http://','')        #규칙1
mystr=mystr[:mystr.index('.')]   #규칙2 mystr[0:5] 직전까지
password = mystr[:3] + str(len(mystr)) + str(mystr.count('e')) + '!'
print('{0}의 비밀번호는 {1} 입니다. ' .format(url,password))
