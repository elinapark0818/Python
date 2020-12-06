class A:
    def __init__(self, value):
        print(1, self)
        self.value = value
        print("A 생성함", self.value)

    def selfTest(self):
        print(self)

class B(A):
    def __init__(self):
        print(2, self)
        A.__init__(self, "FF")
        print("B 생성함")

print("-----------")
b = B()
print("self 테스트")
b.selfTest()
a = A(1)
print("self 테스트")
a.selfTest()