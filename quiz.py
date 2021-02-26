#quiz
# 1."http://naver.com" 에서 http:// 는제외
# 2. .com은 제외
# 3. 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + !
site = "http://naver.com"
pwd = site[7:]
print(site + '\n' + pwd)
pwd = pwd[0:5]      # pwd = pwd[:pwd.index(".")]
print(site + '\n' + pwd)
pwd = pwd[:3] + str(len(pwd)) + str(pwd.count('e')) + "!"
print("{0}의 비밀번호는 {1}".format(site,pwd))