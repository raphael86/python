class Rectangle:
    count = 0   # 클래스 변수 >> 모든 클래스가 공유해요.

    # 초기자(initializer)
    def __init__(self, width, height):
        # self.* : 인스턴스변수 >> 객체마다 값이 달라요.
        self.width = width
        self.height = height
        Rectangle.count += 1
 
    # 메서드
    def calcArea(self):
        area = self.width * self.height
        return area

    # public 메서드
    def publicFunction(self):
        return "public function"

    # public 메서드
    def publicFunctionForPrivateFunction(self):
        return self.__privateFunction()

    # private 메서드
    def __privateFunction(self):
        return "private function"

r1 = Rectangle(1, 2)
r2 = Rectangle(2, 3)

print(r1.count)
print(r2.count)

print("width: %s, height: %s" % (r1.width, r1.height))  # r1 인스턴스 변수 출력
print("width: %s, height: %s" % (r2.width, r2.height))  # r2 인스턴스 변수 출력

print(r1.publicFunction())
print(r1.publicFunctionForPrivateFunction())









