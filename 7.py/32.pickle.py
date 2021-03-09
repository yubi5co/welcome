# pickle : 프로그램상 사용하고 있는 데이터를 파일 형태로 저장하는것
import pickle                                    # wb: w:쓰기 ,b는 바이너리 타입을 의미
profile_file = open('profile.pickle', 'wb')      # 픽클을 쓸려면 항상 바이너리타입을 정리 해줘야 한다.
profile = {'이름':'박명수','나이':30,'취미':['축구','골프','코딩']}  
print(profile)
pickle.dump(profile_file) # profile에 있는 정보를 file에 저장
profile_file.colse()

profile_file = open('profile.pickle', 'rb')    # r: 읽기 
profile = pickle.load(profile_file)            # fild에 있는 정보를 profile에 불러오기
print(profile)
profile_file.close()

