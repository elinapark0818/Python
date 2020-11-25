
num_list = [5,2,7,8,6,4,9]
num_list.sort()
print(num_list) # 작은 숫자가 왼쪽에 오도록 정렬하기

num_list.reverse()
print(num_list) # 큰 숫자가 왼쪽에 오도록 뒤집어서 정렬하기

# 리스트 모두 지우기
num_list.clear()
print(num_list) # 대괄호[] 만 출력된다.

num_list = [1,2,3,4,5,6,7,8,9,10]
mix_list = ["후밍이", "!", 5, False]
print(mix_list)

# 리스트 확장하기
mix_list.extend(num_list)
print(mix_list)