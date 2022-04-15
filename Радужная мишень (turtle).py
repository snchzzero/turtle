import turtle
turtle.up()
turtle.goto(0, -200)
turtle.down()
turtle.hideturtle()
color = ['DeepPink', 'DarkViolet', 'Blue', 'CornflowerBlue', 'cyan', 'LightGreen', 'green', 'yellow', 'orange', 'red']
a, b = 200, -200
for i in range(-1, -(len(color)) - 1, -1):
  turtle.pencolor(color[i])
  turtle.fillcolor(color[i])
  turtle.begin_fill()
  turtle.circle(a)
  turtle.end_fill()
  a -= 20
  b += 20
  turtle.up()
  turtle.goto(0, b)
  turtle.down()