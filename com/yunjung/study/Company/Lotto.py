from random import *
lotto = range(1, 46)
print(lotto)
lotto = list(lotto)
print(lotto)
print('='*10)
shuffle(lotto)
print(lotto)

winner = sample(lotto, 6)

print("--당첨자 발표--")
print("오늘의 로또번호 : {0}".format(winner[0:]))
print("--축하합니다--")