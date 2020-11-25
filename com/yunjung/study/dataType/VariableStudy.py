a = [1,2,3]
b = a
a[1] = 4
print(a)
print(b)

a2 = [1,2,3]
b2 = a2[:]
a2[1] = 4
print(a2)
print(b2)

print(id(a))
print(id(b))
print(a == b)
print(a is b)

from copy import copy
b = copy(a)
print("--------------------")
a, b = ('python', 'life')
a = 'pyhthon'
b = 'life'
print(a)
print(b)
print()