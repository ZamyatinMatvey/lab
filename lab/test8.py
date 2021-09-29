import turtle
window = turtle.Screen()
window.title(u"Черепаха по спирали!")
turtle.shape("turtle")
# y - количество поворотов спирали
# кривизну спирали можно изменять значением постоянного множиеля (5) в функции forward
x = 1
y = int(turtle.textinput(u"Количество поворотов спирали", "Введите желаемое количество поворотов спирали"))
while x <= y:
    turtle.forward(5*x)
    turtle.left(90)
    x += 1
window.exitonclick()