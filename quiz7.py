# 1보다 작거나 문자열이 들어오면 ValueError 처리
#     출력 메시지 : "잘못된 값을 입력."
# 주문할 수 있는 총 치킨량은 10마리
# 치킨 소진시 사용자 정의 에러 SoldOutError 발생 후 프로그램 종료
#     출력 메시지 : "재고가 소진되어 더 이상 주문을 받지 않습니다." 
class SoldOutError(Exception):
    def __init__(self,msg):
        self.msg = msg
    def show(self):
        return self.msg
    
chicken = 10
waiting = 1
while(True):    
    try:
        print("[남은 치킨 : {0}]".format(chicken))
        order = int(input("주문 : "))
        if order < 1:
            raise ValueError
        elif order > chicken or chicken < 1:
            raise SoldOutError("재고가 소진되어 더 이상 주문을 받지 않습니다.")
        else:
            print("[대기번호 {0} {1}마리 주문".format(waiting,order))
            chicken -= order
            waiting += 1
    except ValueError:
        print("잘못된 값 입력")
    except SoldOutError as err:
        print(err)
        break