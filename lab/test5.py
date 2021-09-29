import turtle
t = turtle.Turtle()
t.shape("turtle")

x = 1
y = 20

while x <= 10:
    t.left(225)
    t.penup()
    t.forward((y**2/2)**0.5)
    t.left(135)
    t.pendown()
    t.forward(y*x)
    t.left(90)
    t.forward(y * x)
    t.left(90)
    t.forward(y*x)
    t.left(90)
    t.forward(y*x)
    t.left(90)
    x += 1
turtle.exitonclick()