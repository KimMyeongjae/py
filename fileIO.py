# 파일이름, "w" :쓰기 "a":추가 "r":읽기
# score_file = open("score.txt", "w", encoding="utf-8")
# print("수학 : 0", file=score_file)
# print("영어 : 50", file=score_file)
# score_file.close()

# score_file = open("score.txt", "a", encoding="utf-8")
# score_file.write("과학 : 80")
# score_file.write("\n코딩 : 100")
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf-8")
# print(score_file.read()) 전체 읽어오기 
# print(score_file.readline()) 한줄씩 읽어오기 
# score_file.close()

# 파일이 몇줄인지 모를때
# score_file = open("score.txt", "r", encoding="utf-8")
# while True:
#     line = score_file.readline()
#     if not line:
#         break
#     print(line, end="")
# score_file.close()

# list형태로 저장
# score_file = open("score.txt", "r", encoding="utf-8")
# lines = score_file.readlines() #list 형태
# for line in lines:
#     print(line, end="")
# score_file.close()