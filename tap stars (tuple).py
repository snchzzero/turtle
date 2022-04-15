import turtle
import random
def left_mouse(x, y):
    color = random.choice(["red", "blue", "yellow", "white", "gold", "orange", "green", "pink",
                           "cyan", "gray", "aquamarine", "violet", "chartreuse", "brown", "lawngreen"])
    size = random.randrange(5, 50, 5)
    angle = random. choice([5, 7, 8, 9, 11])
    draw_stars(x, y, angle, size, color)
def draw_stars(x, y, angle, size, color):
    turtle.tracer(10, 5)
    turtle.speed(10)
    turtle.hideturtle()
    turtle.up()
    turtle.goto(x, y)
    turtle.down()
    turtle.pencolor(color)
    turtle.fillcolor(color)
    turtle.begin_fill()
    for i in range(angle):
        turtle.fd(size)
        turtle.left(180 - 180 / angle)
    turtle.end_fill()

turtle.Screen().bgcolor("black")
turtle.Screen().onclick(left_mouse)
turtle.Screen().listen()
turtle.done()
