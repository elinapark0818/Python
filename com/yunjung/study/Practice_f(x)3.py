
# 지역변수와
#
# gun = 10
#
# def checkpoint(soldiers):
#     gun = gun - soldiers
#     print("[함수 내] 남은 총 : {0}".format(gun))
#
# print("전체 총 : {0}".format(gun))
# checkpoint(2)
# print("남은 총 : {0}".format(gun))

print('='*10)

# gun = 10
# def checkpoint(soldiers):
#     gun = 20
#     gun = gun - soldiers
#     print("[함수 내] 남은 총 : {0}".format(gun))
#
# print("전체 총 : {0}".format(gun))
# checkpoint(2)
# print("남은 총 : {0}".format(gun))

# # 전역변수
# gun = 10
# def checkpoint(soldiers):
#     global gun
#     gun = gun - soldiers
#     print("[함수 내] 남은 총 : {0}".format(gun))
#
# print("전체 총 : {0}".format(gun))
# checkpoint(2)
# print("남은 총 : {0}".format(gun))

# gun = 10
# def checkpoint_ret(gun, soldiers):
#     gun = gun - soldiers
#     print("[함수 내] 남은 총 : {0}".format(gun))
#     return gun
# print("전체 총 : {0}".format(gun))
# gun = checkpoint_ret(gun,2)
# print("남은 총 : {0}".format(gun))

# Quiz

def std_wight(height, gender): # 키(m), 성별
    if gender == "남자":
        return height * height * 22
    else:
        return height * height * 21

height = 175 # 키(cm)
gender = "남자"
weight = round(std_wight(height / 100, gender),2)
print("키 {0}m {1}의 표준 체중은 {2}kg 입니다".format(height,gender,weight))