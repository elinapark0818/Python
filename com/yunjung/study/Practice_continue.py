#
# absent = [2,4,6,9,10]
# for number in range(1, 11):
#     if number in absent:
#         continue
#     print("{0}, 왔습니까?".format(number))

absent = [2, 5]
no_book = [7]
for student in range(1, 11):
    if student in absent:
        continue
    elif student in no_book:
        print("오늘 수업 여기까지. {0}는 교무실로 따라와".format(student))
        break
    print("{0}, 일어나서 책 읽어봐".format(student))