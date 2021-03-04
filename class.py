from random import *
class Unit:
    def __init__(self,name,hp,speed): # __init__ -> 생성자
        self.name = name
        self.hp = hp
        self.speed = speed
        print("[{0}] 생성완료".format(name))
    def move(self, location):
        print("{0} : {1}지점으로 이동합니다 [속도{2}]".format(self.name,location,self.speed))
    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name,damage))
        self.hp -= damage
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))
        else:
            print("{0} : 현재 체력은 {1}입니다.".format(self.name,self.hp))            

class AttackUnit(Unit):
    def __init__(self, name, hp,speed,damage):
        Unit.__init__(self,name,hp,speed)
        self.damage = damage 
    
    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]"\
            .format(self.name,location,self.damage))

class Flyable:
    def __init__(self,fly_speed):
        self.fly_speed = fly_speed

    def fly(self,name,location):
        print("{0} : {1}방향으로 출발합니다. [속도{2}]".format(name,location,self.fly_speed))

class FlyalbeAttackUnit(AttackUnit,Flyable):
    def __init__(self,name,hp,damage,fly_speed):
        AttackUnit.__init__(self,name,hp,0,damage)
        Flyable.__init__(self,fly_speed)
    
    def move(self,location):
        self.fly(self.name,location)

class BuildingUnit(Unit):
    def __init__(self,name,hp,location):
        #Unit.__init__(self,name,hp,0)
        super().__init__(name,hp,0)
        self.location = location

class Marine(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self,"마린",40,1,5)
    def stim(self):
        if self.hp > 0:
            self.hp-=10
            print("{0}이 스팀팩 사용".format(self.name))
        else:
            print("{0}이 hp가 부족합니다.".format(self.name))

class Tank(AttackUnit):
    seize_developed = False
    def __init__(self):
        AttackUnit.__init__(self,"탱크",150,1,35)
        self.seize_mode = False
    def set_seize_mode(self):
        if self.seize_developed == False:
            return
        if self.seize_mode == False:
            print("{0} : 시즈모드 전환".format(self.name))
            self.damage *= 2
            self.seize_mode = True
        else:
            print("{0} : 시즈모드 해제".format(self.name))
            self.damage /= 2
            self.seize_mode = False    

class Wraith(FlyalbeAttackUnit):
    def __init__(self):
        FlyalbeAttackUnit.__init__(self,"레이스",80,20,5)
        self.clocked = False
    
    def clocking(self):
        if self.clocked == False:
            print("{0} : 클로킹모드 전환".format(self.name))
            self.clocked = True
        else:
            print("{0} : 클로킹모드 해제".format(self.name))
            self.clocked = False

def game_start():
    print("[알림] 게임을 시작하겠습니다.")
def game_over():
    print("Player : gg")
    print("Player님이 퇴장하셨습니다.")


game_start()

m1 = Marine()
m2 = Marine()
m3 = Marine()

t1 = Tank()
t2 = Tank()
t3 = Tank()

w1 = Wraith()

att = []
att.append(m1)
att.append(m2)
att.append(m3)
att.append(t1)
att.append(t2)
att.append(t3)
att.append(w1)

for i in att:
    i.move("1시")

Tank.seize_developed = True
print("[알림] 탱크 시즈모드 완료")

for i in att:
    if isinstance(i, Marine):
        i.stim()
    elif isinstance(i, Tank):
        i.set_seize_mode()
    elif isinstance(i, Wraith):
        i.clocking()

for i in att:
    i.attack("1시")
for i in att:
    i.damaged(randint(5,30))

game_over()    

