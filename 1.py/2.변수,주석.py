#변수                                                             (어떤 값을 저장하는 공간)

#예) 애완동물을 소개해 주세요~~
print("우리집 강아지의 이름은 연탄이에요")
print("연탄이는 4살이며, 산책을 아주 좋아해요")
print("연탄이는 어른일까요? True")

#변수부분
animal = '고양이'
name = '해피' 
age = 9
hobby = '낮잠'
is_abult = age >= 8

print("우리집 "+animal+"의 이름은 "+name+"에요")                     #+:문장연결
print(""+name+"는 "+str(age)+"살이며, "+hobby+"을 아주 좋아해요")    #str: 정수형을 문자형으로 변환
print(""+name+"는 어른일까요?"+str(is_abult))                    

#주석
#:실행무시,다른사람한테 설명가능 
''':여러문장 무시가능'''