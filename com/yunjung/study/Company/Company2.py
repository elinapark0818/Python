import pickle
profile_file = open("../profile.pickle", "wb")
profile = {"이름":"박엘리나", "나이":29, "취미":["등산", "요리", "코딩"]}
print(profile)
pickle.dump(profile, profile_file)  # profile 에 있는 정보를 file 에 저장한다
profile_file.close()

profile_file = open("../profile.pickle", "rb")
profile = pickle.load(profile_file)  # file 에 있는 정보를 profile 에 불러온다
print(profile)
profile_file.close()

import pickle
with open("../profile.pickle", "rb") as profile_file:
    print(pickle.load(profile_file))

with open("../study.txt", "w", encoding="utf8") as study_file:
    study_file.write("파이썬을 열심히 공부하고 있어요")

with open("../study.txt", "r", encoding="utf8") as study_file:
    print(study_file.read())
#
#
# Quiz) 당신의 회사에서는 매주 1회 작성해야 하는 보고서가 있습니다.
# 보고서는 항상 아래와 같은 형태로 출력되어야 합니다.
#
# - X 주차 주간보고 -
# 부서 :
# 이름 :
# 업무 요약 :
#
# 1주차부터 5주차까지의 보고서 파일을 만드는 프로그램을 작성하시오.
#
# 조건 : 파일명은 '1주차.txt', '2주차.txt', ...와 같이 만드시오.

for i in range(1,6): # 1~5 까지
    with open(str(i) + "주차.txt", "w", encoding="utf8") as report_file:
        report_file.write("- {0} 주차 주간보고 -".format((i)))
        report_file.write("\n부서 :")
        report_file.write("\n이름 :")
        report_file.write("\n업무 요약 :")

#test