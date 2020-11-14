# 함수로 기본값 설정하기

# def profile(name, age, mail_lang):
#     print("이름 : {0}\t나이 : {1}\t사용 언어 : {2}"\
#           .format(name, age, mail_lang))
#
# profile("이후민", 28, "자바")
# profile("박윤정", 29, "파이썬")
# profile("박재상", 26, "C++")
#
# def profile(name, age=20, mail_lang="Python"):
#     print("이름 : {0}\t나이 : {1}\t사용 언어 : {2}"\
#            .format(name, age, mail_lang))
# profile("이후민")
# profile("박윤정")
# profile("박재상")

def profile(name, age, mail_lang):
    print(name, age, mail_lang)

profile(name="박윤정", mail_lang="Python", age=29)
profile(age=26, name="박재상", mail_lang="C++")
profile(mail_lang="Java", age=28, name="이후민")
