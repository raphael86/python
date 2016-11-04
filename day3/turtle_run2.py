import turtle as t

a = t.Turtle() # 주인공
b = t.Turtle() # 악당
c = t.Turtle() # 먹이

a.shape("turtle")    
b.shape("turtle")
c.shape("circle")

a.color("blue")     # 주인공 파란색
b.color("red")      # 악당 빨간색
c.color("green")    # 먹이 초록색

a.speed(0)
b.speed(0)
c.speed(0)

b.up()
b.goto(0, 200)      # 위 방향으로 200 이동

c.up()
c.goto(0, -200)     # 아래 방향으로 200 이동

