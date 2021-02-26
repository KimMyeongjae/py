import pickle
# profile_file = open("profile.pickle", "wb")
# profile = {"이름" : "박명수", "나이" : 30,"취미":["축구","농구","배구"]} 
# print(profile)
# pickle.dump(profile, profile_file) # profile에 있는 정보를 file에 저장
# profile_file.close()

# profile_file = open("profile.pickle","rb")
# profile = pickle.load(profile_file) # file에 있는 정보를 profile에 불로오기
# print(profile)
# profile_file.close()

# with 파일 안닫아도됨
# with open("profile.pickle", "rb") as profile_file:
#     print(pickle.load(profile_file))

# with open("study.txt", "w", encoding="utf-8") as study_file:
#     study_file.write("파이썬을 공부하고 있어요.")

with open("study.txt", "r", encoding="utf-8") as study_file:
    print(study_file.read())