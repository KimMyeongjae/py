#5~15분 소요시간 손님만 탑승


from random import *
cnt = 0 # 탑승 승객 수
for i in range(1,51):
    time = randrange(5,51) #5~50분 소요 시간
    if 5<= time <= 15:
        print("[O] {0}번째 손님 (소요시간 : {1}분".format(i,time))
        cnt += 1
    else:
        print("[] {0}번째 손님 (소요시간 : {1}분".format(i,time))

print("총 탑승 승객수 {0}".format(cnt))