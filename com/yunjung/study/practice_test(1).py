
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

