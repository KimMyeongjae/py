try:
    print("나누기 계산기")
    nums = []
    nums.append(int(input("첫 번째 수 입력 : ")))
    nums.append(int(input("두 번째 수 입력 : ")))
    nums.append(int(nums[0] / nums[1]))
    print("{0} / {1} = {2}".format(nums[0],nums[1],nums[2]))
except ValueError:
    print("잘못된 값 입력 ")
except ZeroDivisionError as err:
    print(err)