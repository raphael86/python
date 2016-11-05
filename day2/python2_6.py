import turtle

turtle.shape("turtle")
turtle.speed(4)



# 궁극의 방법
def drawSomething(size, angle):
   for i in range(angle):
       turtle.forward(size)
       turtle.right(360/angle)

drawSomething(100, 5)
drawSomething(200, 6)
drawSomething(10, 10)




