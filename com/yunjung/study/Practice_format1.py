
# 방법 1
print("나는 %d살입니다." % 29)
print("나는 %s를 사랑해요" % "후민이")
print("후밍이 는 %c로 시작해요." % "후")
# %s 가 많이 쓰인다. 숫자/문자 다 가능하기 때문이다.
print("나는 %s살입니다." % 29)
print("나는 %s와 %s를 좋아해요" % ("후밍이", "후밍이엉덩이"))

print('='*10)

# 방법 2
print("나는 {}살입니다.".format(29))
print("나는 {}색과 {}색을 좋아해요.".format("초록", "검은"))
print("나는 {0}색과 {1}색을 좋아해요.".format("초록", "검은"))
print("나는 {1}색과 {0}색을 좋아해요.".format("초록", "검은"))

print('='*10)

# 방법 3
print("나는 {age}살이며, {color}색을 좋아해요.".format(age = 29, color = "초록"))
print("나는 {age}살이며, {color}색을 좋아해요.".format(color = "초록", age = 29))

print('='*10)

# 방법 4
age = 29
color = "초록"
print(f"나는 {age}살이며, {color}색을 좋아해요.")

print('='*10)