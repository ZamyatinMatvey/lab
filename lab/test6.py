import turtle
t = turtle.Turtle()
t.shape('turtle')
x = 1
while True:
    t.forward(100)
    t.stamp()
    t.backward(100)
    t.right(360 / 12)
    x += 1
    if (x%12) == 1:
        t.clear()