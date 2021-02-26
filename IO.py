# 출력시 , 사용한다면 sep로 ,뒤에 올 문자 결정 end 사용시 문장 끝 부분 결정
# print("Pyton", "Java" , "JavaScript", sep=",")

# 시험 성적
scores = {"수학":0, "영어":50, "코딩":100}
for subject, score in scores.items(): #items -> key, value 쌍으로 
    print(subject.ljust(2), str(score).rjust(4),sep =" :") #n개의 공간은 가진후 정렬


for num in range(1,21):
    print("대기번호 : " + str(num).zfill(3)) # zfill 3개의 공간 확보후 값이 없는공간은 0으로 채운다

# answer = input("아무 값이나 입력하세요 : ")
# print("입력하신 값은 " + answer + "입니다.")

# 빈 자리는 빈공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간을 확보 
print("{0: >10}".format(500))
# 양수일 땐 +로 표시, 음수일 땐 -로 표시
print("{0: >+10}".format(500))
# 왼쪽 정렬하고, 빈칸으로 _로 채움
print("{0:_<+10}".format(5000))
# 3자리 마다 콤마 찍어주기
print("{0:,}".format(1000000000))
# 3자리 마다 콤마 찍어주고 +-부호 붙이기
print("{0:+,}".format(1000000000))
print("{0:+,}".format(-1000000000))
# 3자리 마다 콤마 찍어주고 부호 붙이고 자릿수 확보 빈자리는 ^
print("{0:^<+30,}".format(1000000000))
# 소수점 출력
print("{0:f}".format(5/3))
# 소수정 특정 자리수 까지만 표시 (3째 자리에서 반올림)
print("{0:.2f}".format(5/3))