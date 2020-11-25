# # 출석번호가 1 2 3 4, 앞에 100을 붙이기로 함 > 101, 102, 103, 104
# students = [1,2,3,4,5]
# print(students)
# students = [i+100 for i in students]
# print(students)


# # 문자열을 길이로 변환하기
# students = ["Iron man", "Thor", "I am groot"]
# students = [len(i) for i in students]
# print(students)

# # 이름을 대문자로 변환하기
# students = ["Iron man", "Thor", "I am groot"]
# students = [i.upper() for i in students]
# print(students)

# 이름을 소문자로 변환하기
students = ["Iron man", "Thor", "I am groot"]
students = [i.lower() for i in students]
print(students)
