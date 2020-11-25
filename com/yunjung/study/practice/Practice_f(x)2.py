
# 가변인자

# def profile(name, age, lang1, lang2, lang3, lang4, lang5):
#     print("이름 : {0}\t나이 : {1}\t".format(name,age), end=" ")
#     print(lang1,lang2,lang3,lang4,lang5)
#
# profile("이후민", 28, "Python","Java","C","C++","C#")
# profile("박윤정", 23, "Python", "", "", "" ,"")

def profile(name, age, *language):
    print("이름 : {0}\t나이 : {1}\t".format(name,age), end=" ")
    for lang in language:
        print(lang, end=" ")
    print()

profile("이후민", 28, "Python","Java","C","C++","C#","JavaScript")
profile("박윤정", 23, "Python")