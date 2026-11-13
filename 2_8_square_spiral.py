import turtle
t = turtle.Turtle()
t.pensize(1)
length = 5
for i in range(40):
    t.fd(length)
    t.left(90)
    length += 5
turtle.done()