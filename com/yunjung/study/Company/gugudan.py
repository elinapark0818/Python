
# 구구단 만들기

def GuGu(n):
    result = []
    i = 1
    while i <10:
        result.append(n * i)
        i += 1
    return result
print(GuGu(2))
print(GuGu(3))
print(GuGu(4))
print(GuGu(5))
print(GuGu(6))
print(GuGu(7))
print(GuGu(8))
print(GuGu(9))