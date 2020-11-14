# while = 조건을 설정하는 것
#
# name = "후밍이"
# index = 5
# while index >= 1:
#     print("{0}, 다섯 셀동안 일루 오거라 {1}번 남았따".format(name, index))
#     index -= 1
#     if index == 0:
#         print("일루와 어디갔어?!")

# 무한루프에 빠진 후밍이
# name = "후밍이"
# index = 1
# while True:
#     print("{0}, 후밍이 혼나야대 일루와! {1}대 꿀밤이다.".format(name, index))
#     index += 1

customer = "엘리나"
person = "Unknown"

while person != customer :
    print("{0}, 주문하신 망고 플랫치노 나왔습니다.".format(customer))
    person = input("당신은 누구십니까?")