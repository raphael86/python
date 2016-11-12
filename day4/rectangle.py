#-*- coding: utf-8 -*-

class Rectangle:
    count = 0   # 클래스 변수

    # 초기자(initializer)
    def __init__(self, width, height):
        # self.* : 인스턴스변수
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

r1 = Rectangle(1, 4)
r2 = Rectangle(2, 4)

print(r1.count)         # 클래스 변수 접근 (객체.변수명)
print(r2.count)         # 클래스 변수 접근 (객체.변수명)
print(Rectangle.count)  # 클래스 변수 접근 (클래스명.변수명)

print("width: %s, height: %s" % (r1.width, r1.height))
print("width: %s, height: %s" % (r2.width, r2.height))

print("area: %s" % (r1.calcArea()))
print("area: %s" % (r2.calcArea()))

print(r1.publicFunction())
print(r1.publicFunctionForPrivateFunction())
print(r1.__privateFunction())