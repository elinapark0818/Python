# 1 평균 값 구하기
import a as a

a = 80
b = 75
c = 55
print(a)
print(b)
print(c)
print((a + b + c) / 3)

print('=========================')

# 2 홀수 짝수 구분하기
a = 13
if (a % 2) == 1:
    print("홀수")
else:
    print("짝수")

b = 12
if (b % 2) == 1:
    print("홀수")
else:
    print("짝수")

print('=========================')

# 3 생년월일만 표기하기
a = "881120-1068234"
print(a[0:6])

print('=========================')

# 4 남자 여자 구분하기
a = "881120-1068234"

print(a)

b = a[7]
print(b)
if b == "1":
    print("남자")
else:
    print("여자")

print('==========================')
# 5
a = "a:b:c:d"
b = (a.replace(":", "#"))
print(b)

print('==========================')
# 6
a = [1, 3, 5, 4, 2]
a.sort()
print(a)
a.reverse()
print(a)

print('==========================')
# 7
a = 'lifeistooshort'
print(a)

b = (a[0:3])
b = ",".join('lifeistooshort')
print(b)

print('==========================')

a = ['Life', 'is', 'too', 'short']

# ' ' <- 이 문자로 join한다. ()안에 것들을
b = ' '.join(a)
print(b)

print('==========================')
# 8
a = (1, 2, 3)
print(a)
b = (4, 5)
print(a + b)
b = (4,)
print('=====!!!=====================')
print(a + b)

print('==========================')

# 9
a = dict()
print(a)

# 10
a = {'A':'90','B':'80','C':'70'}
print(a.pop('B'))

# 11

a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
print(type(a))
a = set(a)
print(a)

#12
a = b = [1,2,3]
a[1] = 4
print(b)
#
# # a = [1,2,3]이고
# # b = a 이다
# a[1] = 4 로 하면 a 리스트의 1번째에 위치한 "2" 가 "4"가 된다
# 따라서, a = [1,4,3] 이 되었다
# b = a 이기 때문에
# b = [1,4,3] 으로 출력된다.

print('='*10)

# for while if 연습문제
#
# # 1
# a = "Life is too short, you need python"
# if "wife" in a: print("wife")  # a에 wife가 있다면 wife를 출력해라
# elif "python" in a and "you" not in a:print("python") # a에 python이 있고 you가 없다면 python을 출력해라
# elif "shirt" not in a: print("shirt") # a 에 shirt가 없다면 shirt를 출력해라
# elif "need" in a: print("need") # a에 need가 있다면 need를 출력해라
# else: print("none") # 위 내용이 해당하는게 없다면 none을 출력해라
# # 해당하는 값이 elif "shirt" not in a: print("shirt") 이므로
# # shirt 가 출력된다.
#
# # 2 while 을 사용하여 1부터 1000까지의 자연수 중 3의 배수의 합을 구해 보자
#
# a = 0
# i = 1
# while i <= 1000:
#     if i % 3 == 0:
#         a += i
#     i += 1
# print(a)
#
# a = 0
# i = 1
# while i <= 1000:
#     if i % 3 == 0:
#         a += i
#     i += 1
# print(a)

result = 0
i = 1
while i <= 1000:
    if i % 3 == 0: # 3으로 나누어 떨어지는 수는 3의 배수
        result += i
    i += 1

print(result)