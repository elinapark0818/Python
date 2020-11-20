
# 2
# while
a = 0
i = 1
while i <= 1000:
    if i % 3 == 0: # 3으로 나누어 떨어지는 수는 3의 배수
        a = a + i
    i = i + 1
print(a)

print('='*10)

# for
b = 0
i = 1
for i in range(1, 1001): # 1~1000 까지의 정수
    if i % 3 == 0:
        b = b + i
    i = i + 1
print(b)

print('='*10)

print('''*
**
***
****
*****''')

print('='*10)
# 3
i = 0
while True:
    i = i + 1
    if i > 5: break
    print("*" * i)

print('='*10)

# 4
for i in range(1,101):
    print(i)

print('=' * 10)
# 5
a = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
total = 0
for score in a:
    total = total + score
average = total / len(a)
print(average)

print('=' * 10)
# 6
numbers = [1, 2, 3, 4, 5]
result = []
for n in numbers:
    if n % 2 == 1:
        result.append(n * 2)
print(result)

print('=' * 10)

numbers = [1, 2, 3, 4, 5]
result = [n * 2 for n in numbers if n % 2 == 1]
print(result)

print('='*10)

b = 0
i = 1
for i in range(1, 1001): # 1~1000 까지의 정수
    if i % 3 == 0:
        b = b + i
print(b)