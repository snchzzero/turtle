import turtle
import math
t = 0
turtle.hideturtle()
turtle.speed(0)
turtle.tracer(10,5)
turtle.pencolor("red")
turtle.fillcolor("red")
turtle.begin_fill()
while(t < 2):
    x = 128 * math.sin(t) ** 3
    y = 8 *(13 * math.cos(t) - 5 * math.cos(3 * t) - math.cos(4 * t) - 5)
    turtle.goto(x, y)
    t += 0.01
Xs = x
turtle.goto(0, y - 100)
turtle.goto(-x, y)
t = -2
while(t < 0):
    x = 128 * math.sin(t) ** 3
    y = 8 *(13 * math.cos(t) - 5 * math.cos(3 * t) - math.cos(4 * t) - 5)
    turtle.goto(x, y)
    t += 0.01
turtle.end_fill()
turtle.done()
