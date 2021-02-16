# Quadrant n (제n사분면) 찾기
# qa = x,y 모두 양수
# qb = x 음수 , y 양수
# qc = x,y 모두 음수
# qd = x 양수 , y 음수

#  첫 번째 input은 x값을 입력하도록
#  두 번째 input은 y값을 입력하도록

# 범위 -1000 <= x <== 1000  (x!=0)

# if


x = int(input())
y = int(input())

if x > 0:
    if y > 0:
        print(1)
    else:
        print(4)
else:
    if y > 0:
        print(2)
    else:
        print(3)