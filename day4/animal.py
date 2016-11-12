#-*- coding: utf-8 -*-

class Animal:
    def __init__(self, name):
        self.name = name
    def move(self):
        print("move")
    def speak(self):
        print("mm..")
 
class Dog (Animal):
    def speak(self):
        print("bark")
 
class Duck (Animal):
    def speak(self):
        print("quack")

dog = Dog("개")
duck = Duck("오리")

print(dog.name)
print(duck.name)

dog.speak()
duck.speak()