#1 Hello World!를 출력하시오.

print("Hello World!")

print("="*10)
#2 두 줄에 걸쳐 "강한친구 대한육군"을 한 줄에 한 번씩 출력한다.

print("강한친구 대한육군\n강한친구 대한육군")

print("="*10)
#3 아래 예제와 같이 고양이를 출력하시오.

print("""\\    /\\
 )  ( ')
(  /  )
 \\(__)| """)

print("="*10)
#4 아래 예제와 같이 개를 출력하시오.

print("|\\_/|")
print("|q p|   /}")
print("( 0 )\"\"\"\\")
print("|\"^\"`    |")
print("||_/=\\\\__|")

print("="*10)
# #5 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
# A, B = input().split()
# print(int(A) + int(B))
# #6 A-B
# A, B = input().split()
# print(int(A) - int(B))
# #7 A*B
# A, B = input().split()
# print(int(A) * int(B))
# #8 A/B
# A, B = input().split()
# print(int(A) / int(B))

#9 사칙연산

a, b = input().split()
a = int(a)
b = int(b)
print(a+b, a-b, a*b, int(a/b), a%b, sep = "\n")
