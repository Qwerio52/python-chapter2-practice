import turtle
t = turtle.Turtle()
t.pensize(2)
# 正三角
for i in range(3):
    t.fd(200)
    t.left(120)
# 调转方向画倒三角
t.left(60)
for i in range(3):
    t.fd(200)
    t.left(120)
turtle.done()