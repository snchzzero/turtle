import turtle
turtle.hideturtle()  # невидимая черепашка
turtle.speed(10)

turtle.up()
turtle.goto(-70, -150)
turtle.down()
turtle.heading()
turtle.begin_fill()
for i in range(4):
  if i % 2 == 0:
    turtle.fd(140)
  else:
    turtle.fd(300)
  turtle.left(90)
turtle.end_fill()

turtle.up()
turtle.goto(0, -35)
turtle.down()
turtle.fillcolor("yellow")
turtle.begin_fill()
turtle.circle(40)
turtle.end_fill()

turtle.up()
turtle.goto(0, 50)
turtle.down()
turtle.fillcolor("red")
turtle.begin_fill()
turtle.circle(40)
turtle.end_fill()

turtle.up()
turtle.goto(0, -120)
turtle.down()
turtle.fillcolor("green")
turtle.begin_fill()
turtle.circle(40)
turtle.end_fill()