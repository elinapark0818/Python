# Quadrant n (제n사분면) 찾기
# qa = x,y 모두 양수
# qb = x 음수 , y 양수
# qc = x,y 모두 음수
# qd = x 양수 , y 음수

#  첫 번째 input은 x값을 입력하도록
#  두 번째 input은 y값을 입력하도록

# 범위 -1000 <= x <== 1000  (x!=0)

# if

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
