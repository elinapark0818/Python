#
# print("Python", "Jaba", sep=",")
# print("Python", "Jaba", sep=" vs ")
# print("Python", "Jaba", "JavaScript", sep=" vs ")
# print("Python", "Jaba", "JavaScript", sep=",", end="?")
# print("="*10)
# print("Python", "Jaba", "JavaScript", sep=",",)# end="?")
# print("무엇이 더 재밌을까요?")
#
# print("="*10)
#
# import sys
# print("Python", "Jaba", file=sys.stdout)
# print("Python", "Jaba", file=sys.stderr)

scores = {"수학":0, "영어":50, "코딩":100}
for subject, score in scores.items():
    # print(subject, score)
    print(subject.ljust(8), str(score).rjust(4), sep=":")

print("="*10)

# 은행 대기순번표
# 001, 002, 003, ...
# for num in range(1, 11):
#     print("대기번호 : " + str(num).zfill(3))
#
# answer = input("아무거나 입력해보세요 : ")
# print(type(answer))
# print("입력하신 값은 " + answer +"입니다.")


print("{0: >10}".format(500)) # 오른쪽으로 정렬
print("{0:_<10}".format(500)) # 왼쪽으로 정렬 빈자리 "_"로 채우기

print('='*20)

print("{0:,}".format(10000000000000)) # 3자리마다 콤마 찍기
print("{0:+,}".format(10000000000000)) # 3자리마다 콤마 찍고 +- 부호 붙이기
print("{0:+,}".format(-10000000000000))

print('='*20)

print("{0:^<+30,}".format(10000000000000)) # 3자리마다 콤마 찍고, 빈자리 "^"로 채우고 30자리 확보하고 왼쪽정렬하고 +- 부호 붙이기
print("{0:^<+30,}".format(-10000000000000))

print('='*20)

print("{0:f}".format(5/3)) # 소수점 출력
print("{0:.2f}".format(5/3)) # .2를 f앞에 입력하면 소수점 셋째에서 반올림

print('='*20)

# score_file = open("score.txt", "w", encoding="utf8")
# print("수학 : 0", file=score_file)
# print("영어 : 50", file=score_file)
# score_file.close()

# score_file = open("score.txt", "a", encoding="utf8")
# score_file.write("과학 : 80")
# score_file.write("\n코딩 : 100")
# score_file.close()
#
score_file = open("score.txt", "r", encoding="utf8")
print(score_file.readline()) # 줄별로 읽기, 한줄 읽고 커서는 다음줄로 이동
print(score_file.readline())
print(score_file.readline())
print(score_file.readline())
score_file.close()

print('='*20)

score_file = open("score.txt", "r", encoding="utf8")
print(score_file.readline(), end="") # 줄바꿈 없이
print(score_file.readline(), end="")
print(score_file.readline(), end="")
print(score_file.readline(), end="")
score_file.close()
