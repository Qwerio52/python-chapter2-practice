import turtle

t = turtle.Turtle()
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
t.pensize(20)
t.speed(0)

for i in range(6):
    t.pencolor(colors[i])
    t.fd(40)
    t.left(60)
turtle.done()