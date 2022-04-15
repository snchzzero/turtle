import turtle
turtle.hideturtle()
for i in range(3):
  turtle.fd(150)
  turtle.left(120)

a = 20
turtle.fillcolor("black")
turtle.up()
turtle.goto(0, 55)
turtle.down()
turtle.begin_fill()
turtle.circle(a)
turtle.end_fill()

turtle.up()
turtle.goto(150, 55)
turtle.down()
turtle.begin_fill()
turtle.circle(a)
turtle.end_fill()

turtle.up()
turtle.goto(75, -75)
turtle.down()
turtle.begin_fill()
turtle.circle(a)
turtle.end_fill()

turtle.penup()
turtle.goto(0, 75)
turtle.down()
turtle.pencolor("white")
turtle.fillcolor("white")
turtle.begin_fill()
for i in range(3):
  turtle.fd(150)
  turtle.right(120)
turtle.end_fill()