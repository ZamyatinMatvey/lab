import turtle
import math
window = turtle.Screen()
window.title(u"Черепаха по спирали!")
turtle.shape("turtle")
turtle.speed(0)
# y - количество поворотов спирали
# кривизну спирали можно изменять значением постоянного множиеля (5) в функции forward
x = 0
while True:
    turtle.forward(x / 2 *  math.pi)
    turtle.left(2 * math.pi)
    x += 0.01
window.exitonclick()

