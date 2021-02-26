# {key:value} 정수 문자열 다 가능
cabinet = {3:"유재석",4:"김태호"}
print(cabinet[4])
print(cabinet.get(5, "없음")) # get사용이 값 없을때 없음출력

print(3 in cabinet) # 3이라는 key값이 있는지
print(5 in cabinet)

#추가
cabinet[3] = "김종국"
cabinet[5] = "조세호"
print(cabinet)
#삭제
del cabinet[3]
print(cabinet)
# key, value 출력
print(cabinet.keys())
print(cabinet.values())
print(cabinet.items())
#모두삭제
cabinet.clear()
print(cabinet.items())

#튜플은 변경 x (value,value) 여러개 가능
menu = ("돈까스", "치즈까스")
print(menu[0])
print(menu[1])
(menu, price, count) = ("왕돈까스",10000,5)
print(menu,price,count)