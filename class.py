class Unit:
    def __init__(self,name,hp,damage): # __init__ -> 생성자
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성 되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

# marine1 = Unit("마린",40,5)
# marine2 = Unit("마린",40,5)
# tank = Unit("탱크",150,35)
# tank2 = Unit("탱크",150,35)

# wraith1 = Unit("레이스",80,5)
# print("유닛 이름 : {0}, 공격력 : {1}".format(wraith1.name,wraith1.damage))
# wraith1.clocking = True

# if wraith1.clocking == True:
#     print("{0} 는 현재 클로킹입니다.".format(wraith1.name))


class AttackUnit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage 
    
    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]"\
            .format(self.name,location,self.damage))
    
    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name,self.damage))
        self.hp -= damage
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))
        else:
            print("{0} : 현재 체력은 {1}입니다.".format(self.name,self.hp))

firebat1 = AttackUnit("파이어뱃", 50, 16)
firebat1.attack("5시")
firebat1.damaged(14)
firebat1.damaged(25)
firebat1.damaged(14)