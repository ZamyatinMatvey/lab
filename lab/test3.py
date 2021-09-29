import turtle
t = turtle.Turtle()
t.shape('turtle')
x = 1
while True:
    t.forward(100)
    t.left(90)
    x = x + 1
    if (x % 4) == 1:
        t.clear()