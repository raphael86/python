import turtle
import os

# 배경 설정
screen = turtle.Screen()
screen.bgcolor("lightgreen")
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

# 배경음악 설정
# os.system("start c:/python/day5/intro.mp3")

# 플레이어
player = turtle.Turtle()
player.color("blue")
player.shape("triangle")
player.penup()

# 스피드 설정하기
speed = 1

# 컨트롤 함수 정의
def turnLeft():
  player.left(20)

def turnRight():
  player.right(20)

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