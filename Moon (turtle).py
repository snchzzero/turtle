import turtle
moon = turtle.Turtle()
shadow1 = turtle.Turtle()
shadow2 = turtle.Turtle()

shadow1.hideturtle()
shadow1.pensize(155)
shadow1.pencolor("Blue")
shadow2.hideturtle()
shadow2.pensize(155)
shadow2.pencolor("Blue")

moon.hideturtle()
turtle.Screen().bgcolor("Blue")
moon.pencolor("Gold")
moon.pensize(150)
moon.dot()

a = 250
for i in range(280):
  if a > 0:
    shadow1.up()
    shadow1.goto(a, 0)
    shadow1.down()
    shadow1.dot()
  elif a == 0 or a < 0:
    shadow1.up()
    shadow2.up()
    shadow1.goto(a, 0)
    shadow2.goto(a, 0)
    shadow1.down()
    shadow2.down()
    shadow1.dot()
    shadow2.dot()
    shadow1.clear()
    shadow1.dot()
    shadow2.clear()
  a -= 5
