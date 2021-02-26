# n주차 보고서 작성
import pickle
for i in range(1,3):
    with open(str(i) + "주차 보고서", "w", encoding="utf-8") as report:
        report.write("{0}주차 보고\n".format(i))
        report.write("부서 : \n")
        report.write("이름 : \n")
        report.write("업무요약 : \n")