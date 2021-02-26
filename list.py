# 리스트 [] = 배열 여러 자료형 함께 사용

subway = [10, 20, 30]
print(subway)

subway = ["유재석", "조세호", "박명수"]
print(subway)
print(subway.index("유재석")+1)

subway.append("하하") #맨뒤에 삽입
print(subway)

subway.insert(1,"정형돈") #사이에 삽입 (index,값)
print(subway)

print(subway.pop()+"삭제") #맨뒤에꺼 삭제
print(subway)

subway.append("유재석")
print(subway)
print(subway.count("유재석")) #같은이름의 사람이 몇 명인지

#정렬
nlist = [5,3,8,1,6,4]
nlist.sort()
print(nlist)
#뒤집기
nlist.reverse()
print(nlist)
#모두 지우기
# nlist.clear()
# print(nlist)

#리스트 확장
nlist.extend(subway)
print(nlist)