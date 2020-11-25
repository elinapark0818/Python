
# 집합 (set)
# 중복 불가
# 순서 없음

my_set = {42, 5, 12, 12, 41, 41, 42}
print(my_set)

print('='*10)

java = {"이후민", "이새한", "엄지용"}
python = set(["박윤정", "이후민"])

# 교집합 (java와 python을 모두 할 수 있는 개발자)
print(java & python) # 이후민
print(java.intersection(python)) # 이후민

# 합집합 (java를 할 수 있거나 python을 할 수 있는 개발자)
print(java | python)
print(java.union(python))

# 차집합 (java는 할 수 있지만 python은 할 수 없는 개발자)
print(java - python)
print(java.difference(python))

# python 할 수 있는 개발자 추가하기
python.add("신민우")
print(python)

# java를 할 수 있는 개발자 퇴사했음. 삭제하기
java.remove("엄지용")
print(java)