#quiz
#20명 중 1명은 치킨 3명은 커피
#중복 불가
#random 모듈의 shuffle과 sample 활용

from random import *
ilist = range(1,21) # 1부터 21까지 생성
ilist = list(ilist)
print(ilist)
shuffle(ilist) #list값 무작위로 섞음
print(ilist)
winner = sample(ilist, 4) #list값중 무작위로 하나 뽑음
print("-- 당첨자 발표 -- ")
print("치킨 당첨자 : {0}".format(winner[0]))
print("커피 당첨파 : {0}".format(winner[1:]))
print("-- 축하합니다 --")