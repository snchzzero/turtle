import turtle
total = 0
size = 50
x, y = -150, 150
turtle.up()
turtle.goto(x, y)
turtle.down()
turtle.hideturtle()
turtle.speed(0)

def black(size):
    turtle.fillcolor("black")
    turtle.begin_fill()
    for i in range(4):
        turtle.fd(size)
        turtle.left(90)
    turtle.end_fill()
    turtle.fd(size)

def white(size):
    #turtle.fillcolor("white")
    #turtle.begin_fill()
    for i in range(4):
        turtle.fd(size)
        turtle.left(90)
    #turtle.end_fill()
    turtle.fd(size)

for row in range(5):
    for colomn in range(5):
        if total % 2 == 0:
            black(size)
        else:
            white(size)
        total += 1
    turtle.up()
    y -= 50
    turtle.goto(x, y)
    turtle.down()
