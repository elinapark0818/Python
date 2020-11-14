
subway = ["이후민", "박윤정", "이윤지"]
print(subway)

# 이후민은 몇 번째에 있습니까?
print(subway.index("이후민")) # 0번째에 타고 있습니다.
print(subway.index("이윤지"))
print(subway.index("박윤정"))

# 박재상이 다음 정류장에서 맨 뒤에 탐
subway.append("박재상")
print(subway)

# 박엘리나가 다음 정류장에서 이윤지 / 박재상 사이에 탐
subway.insert(3, "박엘리나")
print(subway)

# 다음정류장에서 이후민이 내림
subway.remove("이후민")
print(subway)