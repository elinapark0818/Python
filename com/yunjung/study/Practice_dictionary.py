box = {1:"후밍이", 2:"윤지", 3:"재상이", 4:"윤정이"}
print(box[2])
print(box[1])
print(box[4])
print(box[3])

print(box.get(3))
# print(box[5]) # 5라는 Key 는 없어서 KeyError 발생

print(box.get(5)) # 5 가 없어서 None 출력
print(box.get(5, "형원이"))
print("Hi")

print(3 in box) # True
print(9 in box) # False

print('='*10)

box = {"A-1":"이후민", "A-2":"박윤정", "B-1":"박재상", "B-2":"이윤지"}
print(box)
print(box["A-2"])
print(box["B-1"])

print(box)
box["A-1"] = "몽쭁이"  # 이후민 대신 몽쭁이가 "A-1"에 탄다
box["C-1"] = "후밍이"  # 후밍이가 탄다
print(box)

del box["B-1"]        # 박재상이 내린다.
print(box)
del box["A-1"]        # 몽쭁이가 내린다
print(box)

# key 들만 출력하기
print(box.keys())
# value 들만 출력하기
print(box.values())
# key, value 쌍으로 출력하기
print(box.items())