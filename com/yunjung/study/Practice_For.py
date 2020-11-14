# print("대기번호 : 1")
# print("대기번호 : 2")
# print("대기번호 : 3")
# print("대기번호 : 4")

# for waiting in [0,9,8,7,6,3,1,2,3,4,5]:
#     print("대기번호 : {0}".format(waiting))

for waing in range(1,6): # 1 ~ 5
    print("대기번호 : {0}".format(waing))

starbucks = ["후밍이", "엘리나", "윤정이", "스테파노"]
for customer in starbucks:
    print("{0}, 커먼 베이비 음료 받아가랏".format(customer))