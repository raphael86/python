import turtle as t

b = t.Turtle() # 악당
c = t.Turtle() # 먹이

t.shape("turtle")    
b.shape("turtle")
c.shape("circle")

t.color("blue")     # 주인공 파란색
b.color("red")      # 악당 빨간색
c.color("green")    # 먹이 초록색

t.speed(0)
b.speed(0)
c.speed(0)

b.up()
b.goto(0, 200)      # 위 방향으로 200 이동

c.up()
c.goto(0, -200)     # 아래 방향으로 200 이동

def turn_right():
  t.setheading(0)
  t.forward(10)

def turn_left():
  t.setheading(180)
  t.forward(10)

def turn_up():
  t.setheading(90)
  t.forward(10)

def turn_down():
  t.setheading(270)
  t.forward(10)

t.onkeypress(turn_right, "Right")
t.onkeypress(turn_left, "Left")
t.onkeypress(turn_up, "Up")
t.onkeypress(turn_down, "Down")
t.listen()
