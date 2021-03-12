
# 여러 개의 소금물을 섞었을 때, 혼합된 소금물의 퍼센트 농도와 양을 계산하는 프로그램을 만드시오.

inputs = []
for i in range(10):
    s = input('농도(%)와 소금물의 양(g)을 입력하세요: ')
    if s == 'end':
        break
    inputs.append(s)

total_salt = 0
total_water = 0
for i in inputs:
    s = i.split(' ')
    water = float(s[1][:-1])
    salt = water * float(s[0][:-1]) / 100
    total_salt += salt
    total_water += water

salt_ratio: float = round(total_salt / total_water * 100, 2)
total_water = round(total_water, 2)
print('{}% {}g'.format(salt_ratio, total_water))
