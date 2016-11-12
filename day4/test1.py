class FourCal:
    def setdata(self, first, second):
        # 데이터를 셋팅하는 클래스 함수
        self.first = first
        self.second = second
    def sum(self):
        # 클래스 변수를 더하는 함수
        result = self.first + self.second
        return result
    def mul(self):
        # 클래스 변수를 곱하는 함수
        result = self.first * self.second
        return result
    def sub(self):
        # 클래스 변수를 빼는 함수
        result = self.first - self.second
        return result
    def div(self):
        # 클래스 변수를 나누는 함수
        result = self.first / self.second
        return result

# 정의된 클래스를 객체로 만들자

cal1 = FourCal()        # cal1 객체 생성
cal2 = FourCal()        # cal2 객체 생성
cal1.setdata(40, 20)
cal2.setdata(20, 5)
print("%d, %d, %d, %d" % (cal1.sum(), cal1.mul(), cal1.sub(), cal1.div()))
print("%d, %d, %d, %d" % (cal2.sum(), cal2.mul(), cal2.sub(), cal2.div()))
