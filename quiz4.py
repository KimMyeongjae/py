def std_weight(height,gender):
    if gender == "남자":
        return float(height/100 * height/100 * 22)
        
    elif gender == "여자":
        return float(height/100 * height/100 * 21)

print("{0}cm {1}의 표준 체중은 {2}kg입니다".format(175,"남자",round(std_weight(175,"남자"),2)))   #round(),2 3번째 자리에서 반올림