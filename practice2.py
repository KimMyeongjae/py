#%d %s사용시 문자열 뒤에 %사용
#두가지 사용시 ("a","b")
print("나는 %d살입니다."%20)
print("나는 %s을 좋아아해요"%"python")

#중괄호 사용 .format()사용 {0} {1} format("a","b") index
print("나는 {}살입니다.".format(20))

#format 안의 key사용
print("나는 {age}살이고 {city}에산다.".format(age = 26, city="양산"))

#print문에서 f로 사용 format사용 안해도됨
age =26
city = "양산"
print(f"나는 {age}살,{city}거주")

#다주인용부호 -> \사용 \r 맨앞으로 이동 \b 한글자 삭제

