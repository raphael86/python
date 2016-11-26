import turtle
import os
import math
import random

# 배경 설정
screen = turtle.Screen()
screen.bgcolor("lightgreen")
screen.title("Turtle Run Ver.1")
screen.tracer(2)

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

# 여러 개의 먹이 만들기
maxGoals = 10
goals = []

for count in range(maxGoals):
  # 먹이생성
  goals.append(turtle.Turtle())
  goals[count].color("red")
  goals[count].shape("circle")
  goals[count].penup()
  goals[count].speed(0)
  goals[count].setposition(random.randint(-300, 300), random.randint(-300, 300))
  goals[count].right(random.randint(0, 360))

# 스피드 설정하기
speed = 1

# 점수
score = 0

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

def isCollision(t1, t2):
  # sqrt 는 루트 근사값을 구하는 함수
  # t1, t2를 기준으로 정사각형의 한 변 근사값을 구한다.
  val = math.sqrt(math.pow(t1.xcor() - t2.xcor(), 2) + math.pow(t1.ycor() - t2.ycor(), 2))
  if val < 20:
    return True
  else:
    return False

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

  # 먹이감을 움직인다.
  for count in range(maxGoals):
    goals[count].forward(2)

    # 먹이 가장자리 이탈 확인 및 충돌음 설정
    if goals[count].xcor() > 290 or goals[count].xcor() < -290:
      goals[count].right(180)

    if goals[count].ycor() > 290 or goals[count].ycor() < -290:
      goals[count].right(180)
    # 플레이어-먹이 충돌 확인 및 점수판에 글자 그리기
    if isCollision(player, goals[count]):
      goals[count].setposition(random.randint(-300, 300), random.randint(-300, 300))
      goals[count].right(random.randint(0, 360))
      score += 1
      mypen.undo()
      mypen.penup()
      mypen.hideturtle()
      mypen.setposition(-290, 310)
      scorestring = "Score: %s" %score
      mypen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))