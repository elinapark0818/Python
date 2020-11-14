# weather = "비"
# # weather = "미세먼지"
# A = "맑음"
# if A == "비":
#     print("우산을 챙기세요")
# # elif A == "미세먼지":
# #     print("마스크를 챙기세요")
# else:
#     print("준비물이 필요하지 않아요")

# input

# weather = input("오늘 날씨는 어때요?")
# if weather == "비" or weather == "눈":
#     print("우산을 챙기세요.")
# elif weather == "미세먼지":
#     print("마스크를 착용하세요.")
# else:
#     print("화창합니다.")

# int

temp = int(input("오늘 기온은 어때요?"))
if 30 <= temp:
    print("너무 더워요.")
elif 10 <= temp and temp < 30:
    print("괜찮은 온도에요.")
elif 0 <= temp < 10:
    print("쌀쌀해요. 외투를 입으세요.")
else:
    print("너무 추워요.")