def open_account():
    print("새로운 계좌가 생성되었습니다.")
def deposit(balance, money):
    print("입금이 완료되었습니다 잔액은{0}원 입니다.".format(balance + money))
    return balance + money

def withdraw(balance,money):
    if balance >= money:
        print("출금이 완료되었습니다. 잔액은 {0}원".format(balance - money))
        return balance - money
    else:
        print("출금이 완료되지 않았습니다. 잔액은 {0}원".format(balance))
        return balance

def withdraw_night(balance,money):
    commission = 100
    return commission, balance - money - commission

balance = 0
balance = deposit(10000,5000)
balance = withdraw(balance,6000)
balance = withdraw(balance,16000)
commission, balance = withdraw_night(balance, 500)
print("수수료 {0}원이며, 잔액은 {1}원 입니다,".format(commission,balance))

def profile(name, age, *lang):  #*를 붙이면 같은 변수지만 여러개 가능
    print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ") #end=" " 줄바꾸지 않음
    for i in lang:
        print(i, end=" ")
    print()

profile("유재석",20,"Python","Java","C","C++","C#","JavaScript")
profile("김태호",25,"Kotlin","Swift")