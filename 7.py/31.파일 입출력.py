# 파일 입출력
score_file = open('score.txt','w', encoding='utf8')  # utf8: 한글 출력할떄, w: (덮어)쓰기
print('수학:0',file=score_file)
print('영어:50',file=score_file)
score_file.close()                                    # .close(): 파일을 닫아줘야 한다

score_file = open('score.txt','a', encoding='utf8') # a: 이어쓰기
score_file.write('과학 : 80')
score_file.write("\n코딩 : 100")
score_file.close()

score_file = open('score.txt','r', encoding='utf8') # r: 읽기
print(score_file.read())
score_file.close()

score_file = open('score.txt','r', encoding='utf8') 
print(score_file.readline())  # readline: 줄별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
print(score_file.readline())
print(score_file.readline())
print(score_file.readline())
score_file.close()

# 파일이 몇줄인지 모르는 경우
score_file = open('score.txt','r', encoding='utf8')
while True:
    line = score_file.readline()
    if not line:
        break
    print(line)
score_file.close

# readlines() 모든라인을 가져와서 list형태로 저장
score_file = open('score.txt','r', encoding='utf8')
lines = score_file.readlines() 
for line in lines:
    print(line,end="")

score_file.close