# A, B = list(input().split())
# Min = 50
#
# for i in range(len(B) - len(A) + 1):
#     count = 0
#     for j in range(len(A)):
#         if A[j] != B[i + j]:
#             count += 1
#     if count < Min:
#         Min = count
# print(Min)

A, B = input().split()
_min = len(A)
for j in range(len(B) - len(A) + 1):
    count = 0
    for i in range(len(A)):
        if A[i] != B[i + j]:
            count += 1
    if count < _min:
        _min = count
print(_min)
