import turtle
size = 200
x, y = -100, -150
turtle.speed(10)
turtle.tracer(10, 5)
turtle.hideturtle()
color = ['black', 'white', 'red']
for clr in color:
    turtle.pencolor(clr)
    turtle.up()
    turtle.fillcolor(clr)
    turtle.goto(x, y)
    turtle.down()
    turtle.begin_fill()
    for i in range(8):
        turtle.fd(size)
        turtle.left(360 / 8)
    turtle.end_fill()
    x += 2.5
    y += 5
    size -= 5
turtle.up()
turtle.goto(x + 100, y + 130)
turtle.down()
turtle.pencolor("white")
turtle.write("STOP", align="center", font=('Arial', 120, 'bold'))
turtle.done()




