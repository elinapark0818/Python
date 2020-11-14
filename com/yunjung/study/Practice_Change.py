
# 자료구조의 변경

menu = {"아이스티", "쑥라떼", "천혜향에이드"}
print(menu, type(menu))

menu = list(menu)
print(menu, type(menu))

menu = tuple(menu)
print(menu, type(menu))

menu = set(menu)
print(menu, type(menu))