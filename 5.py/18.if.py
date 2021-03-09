# if 조건문
weather = input('오늘 날씨는 어때요')
if weather == '비' or weather == '눈':
    print('우산을 챙기세요')
elif weather == '미세먼지':       
    print('마스크 챙기세요')
else:                            #아무 해당사항이 없을떄
    print('준비물 챙기세요')    


temp = int(input('기온은 어때요?')) #기온은 숫자이기 때문에 int로 감싸야함
if 30 <= temp:
    print('너무 더워요 나가지 마세요')
elif 10 <= temp and temp < 30:
    print('괜찮은 날씨에요')
elif -20 <= temp and temp < 10:
    print('외투를 챙기세요')
else:
    print('너무 추워요 나가지 마세요')
