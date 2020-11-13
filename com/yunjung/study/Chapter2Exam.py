# 1
국어 = 80
영어 = 75
수학 = 55
print((국어 + 영어 + 수학) / 3)

# 2

a = 13
print(a % 2 == 0)
print("--------------")
if a % 2 == 0:
    print("짝수")
else:
    print("홀수")

# 1 = true, 0 = false
if a % 2:
    print("홀수")
else:
    print("짝수")


# 3

a = "881120-1068234"
print(a)
print(a[:6])
print(a[7:])
split = a.split("-")
print(split)
print("-----------")
for item in split:
    print(item)

print("--------------")
# 4

a = "881120-1068234"
print(a[7])
if a[7]==1:
    print("남자")
else:
    print("여자")
print('================================')
a = "881120-2068234"
print("이게 뭐가 나올까?")
print(a[7])
# 방법 1: 문자를 숫자로 변환한다. int()
# 이것도 나쁘진 않아 3이랑 4 예외케이스를 잘 짚었어.
# 쉬운거로 간다면 그냥 7번째가 1이면 남자 2면 여자
# a[7]이 2와 같나?
print(a[7] == 2)
if a[7] == 2:
    print("여자")
else:
    print("남자")

# 5

a = "a:b:c:d"
b = a.replace(":","#")
print(b)

print("fffffffffff")
a = "a:b:c:d"
b = a.replace(":","#")
print(a)
print(b)