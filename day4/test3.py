class Unit:
    count = 0

    def __init__(self, name):
        Unit.count = Unit.count + 1
        self.name = name
        
    def move(self):
        print("이동합니다")

    def speak(self):
        print("크아앙")
 
class Dron(Unit):
    def speak(self):
        print("퉤엣..")
 
class Hydra(Unit):
    def speak(self):
        print("퉥퉥퉥")


d1 = Dron("드론1")
d2 = Dron("드론2")
h1 = Hydra("히드라1")
h2 = Hydra("히드라2")

d1.move()
d1.speak()
h2.move()
h2.speak()

print("현재인구수:%d" % (Unit.count))
