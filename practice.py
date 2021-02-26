#랜덤 이용 퀴즈
#랜덤 사용시 from random import *
#randint(a,b) -> a와 b사이의 정수 랜덤출력
from random import *
day = randint(4,28)
print("오프라인 스터디 모임 날짜는 매월" + str(day) + "일로 선정되었습니다.")

# """ 따옴표 3개안에서는 줄바꿈 가능
sentence = """
김
명
재
"""
print(sentence)

#슬라이싱 문자열도 배열처럼 취급
#배열[0:2] 0번째부터 2번째 앞까지  [:x] 처음부터 x앞까지 [x:] x부터 끝까지
jumin = "123123-4567890"
print("성별 : " + jumin[7])
print("연도 : " + jumin[0:2])

#문자열 소문자 lower() 대문자 upper()
#isupper() 대문자확인 len()문자열 길이
#replace(a,b) a를 b로 변환 
#index("x") x가 어느 인덱스자리에 있는지
#find index와 동일하나 오류가나면 -1 index는 오류출력
#count("x") x가 몇개 나오는지 
python = "Python Lang"
print(python.lower())
print(python.upper())
print(len(python))