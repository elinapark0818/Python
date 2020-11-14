
# url : http://naver.com
#
# 규칙 1 : http:// 삭제 >> naver.com
# 규칙 2 : 처음 만나는 점(.) 이후 삭제 >> naver
# 규칙 3 : 남은 글자 중 처음 세 자리 + 글자 총 개수 + 글자 내 'e' 개수 + "!" 로 구성
#                   (nav)              (5)          (1)         (!)
# 예) 생성된 비밀번호 : nav51!

url = "http://naver.com"
my_str = url.replace("http://", "")
print(my_str)                        # 규칙 1 완성

print('='*10)

my_str = my_str[:my_str.index(".")]
print(my_str)                       # 규칙 2 완성

print('='*10)

password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
print("{0} 의 비밀번호는 {1} 입니다.".format(url, password))