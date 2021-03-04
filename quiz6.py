#총 3대의 매물
# 강남 오피스텔 매매 10억 2010년
# 마포 오피스텔 전세 5억 2007년
# 송파 빌라 월세 500/50 2000년

class House:
    def __init__(self,location,htype,dtype,price,year):
        self.location = location
        self.htype = htype
        self.dtype = dtype
        self.price = price
        self.year = year

    def show(self):
        print(self.location, self.htype, self.dtype, self.price, self.year)

houses = []
houses1 = House("강남","오피스텔","매매","10억","2010년")
houses2 = House("마포","오피스텔","전세","5억","2007년")
houses3 = House("송파","빌라","월세","500/50","2000년")

houses.append(houses1)
houses.append(houses2)
houses.append(houses3)

print("총 {0}대의 매물".format(len(houses)))
for i in houses:
    i.show()