import turtle
t = turtle.Turtle()
t.pensize(2)
# 外层大三角
for i in range(3):
    t.fd(200)
    t.left(120)
# 移动到内部起点
t.penup()
t.fd(100)
t.left(60)
t.pendown()
# 内层倒三角
for i in range(3):
    t.fd(100)
    t.left(120)
turtle.done()