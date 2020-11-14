python = "Python is Amazing"
print(python.lower()) # 전부 소문자로 바꾸기
print(python.upper()) # 전부 대문자로 바꾸기
print(python[0].isupper()) # 대문자가 맞으면 true
print(len(python)) # 길이구하기
print(python.replace("Python", "Java")) # 다른 문자열로 바꾸기

index = python.index("n")  # 문자의 위치찾기
print(index)
index = python.index("n", index + 1) # 찾은 문자의 위치+1 이후 문자의 위치 찾기
print(index)

# print(python.find("Java")) # find는 해당하는 문자가 없다면 -1 출력한다.
# print(python.index("Java")) # index는 해당하는 문자가 없다면 에러 발생한다.

# Ctrl + / = 주석 처리하기
# Shift + home 또는 end = 문장 처음 또는 끝까지 선택
# Ctrl + Shift + 방향키 = 문장 위치 옮기기
