import turtle
t = turtle.Turtle()
t.shape("turtle")
t.speed(0)
x = 1
while True:
    t.forward(2)
    t.left(1)
    if (x%360) == 1:
        t.clear()
    x += 1