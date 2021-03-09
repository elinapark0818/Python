year = 0

year = int(input("연도를 입력하세요(윤년계산기) : "))
if (((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0)):
    print("1")
else:
    print("0")
# for year in range(1,4000):

a = int(input())
if (a % 4 == 0 and a % 100 != 0) or a % 400 == 0:
    print(1)
else:
    print(0)


x = int(input("x값을 입력하세요."))
y = int(input("y값을 입력하세요."))
if x == 0 or y == 0:
    print("0이 아닌 다른 수를 입력하세요.")
elif x > 0 and y > 0:
    print("제 1사분면입니다.")
elif x < 0 and y > 0:
    print("제 2사분면입니다.")
elif x > 0 and y < 0:
    print("제 4사분면입니다.")
else:
    print("제3사분면입니다.")
