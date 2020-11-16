# # while = 조건을 설정하는 것
# #
# # name = "후밍이"
# # index = 5
# # while index >= 1:
# #     print("{0}, 다섯 셀동안 일루 오거라 {1}번 남았따".format(name, index))
# #     index -= 1
# #     if index == 0:
# #         print("일루와 어디갔어?!")
#
# # 무한루프에 빠진 후밍이
# # name = "후밍이"
# # index = 1
# # while True:
# #     print("{0}, 후밍이 혼나야대 일루와! {1}대 꿀밤이다.".format(name, index))
# #     index += 1
#
# # customer = "엘리나"
# # person = "Unknown"
# #
# # while person != customer :
# #     print("{0}, 주문하신 망고 플랫치노 나왔습니다.".format(customer))
# #     person = input("당신은 누구십니까?")
# #
# #
#
# def solution(v):
#     answer = []
#     v1 = []
#     v2 = []
#     for i in v:
#         if i[0] not in v1:
#             v1.append(i[0])
#         else:
#             v1.remove(i[0])
#         if i[1] not in v2:
#             v2.append(i[1])
#         else:
#             v2.remove(i[1])
#     answer = v1 + v2
#     return answer
#
# solution([[1, 4], [3, 4], [3, 10]])
# solution([[1, 1], [2, 2], [1, 2]])
#
# #
# # while문을 사용해 1부터 1000까지의 자연수 중 3의 배수의 합을 구해 보자.
# #
# result = 0
# i = 1
# while i <= 1000:
#     if i % 3 == 0:
#         result = result + i
#     i = i + 1
# print(result)
#
# print('='*10)
#
# a = range(1, 1001)
# result = 0
# for item in a:
#     if item % 3 == 0:
#         result += item
#     last = result
# print(result)
#
# # while문을 사용하여 다음과 같이 별(*)을 표시하는 프로그램을 작성해 보자
#
#
# a = str("*")
# print("*\n","**\n","***\n","****\n","*****\n","******\n","*******\n")
# # b =
# # '''
# # *
# # **
# # ***
# # ****
# # '''
# # print(b)
# #
# #
# print("=============")
# a = "*"
# i = 1
# while i <= 5:
#     print(a)
#     a += "*"
#     i += 1
# print("=============")
# a = range(1, 1001)
# result = 0
# for item in a:
#     if item % 3 == 0:
#         result += item
# print(result)

a = ["*","*","*","*","*","*"]
star = "*"
for i in a:
    print(star)
    star += "*"
print(star)