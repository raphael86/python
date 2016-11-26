#-*- coding: utf-8 -*-

import turtle

# 배경설정
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Turtle Run Ver.1")

# 가장자리 그리기
mypen = turtle.Turtle()
mypen.penup()
mypen.setposition(-300, -300)
mypen.pendown()
mypen.pensize(3)
for side in range(4):
  mypen.forward(600)
  mypen.left(90)
mypen.hideturtle()


# 플레이어
player = turtle.Turtle()
player.color("blue")
player.shape("triangle")
player.penup()

# 먹이
goal = turtle.Turtle()
goal.color("red")
goal.shape("circle")
goal.penup()
goal.speed(0)
goal.setposition(-100, -100)

# 스피드 설정하기
speed = 1

# 컨트롤 함수 정의
def turnLeft():
  player.left(30)

def turnRight():
  player.right(30)

def speedUp():
  global speed
  speed += 1

def speedDown():
  global speed
  speed -= 1

# 키보드 바인딩
turtle.listen()
turtle.onkey(turnLeft, "Left")
turtle.onkey(turnRight, "Right")
turtle.onkey(speedUp, "Up")
turtle.onkey(speedDown, "Down")

while True:

  # 플레이어 이동
  player.forward(speed)

  # 가장자리 이탈 확인
  if player.xcor() > 300 or player.xcor() < -300:
    player.right(180)

  if player.ycor() > 300 or player.ycor() < -300:
    player.right(180)












