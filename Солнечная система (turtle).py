import turtle
import math
turtle.tracer(10, 5)
turtle.speed(10)
turtle.hideturtle()
x, y = -450, 0
size1 = 2
planet = {"Солнце": {"color": "gold", "size": 50}, "Меркурий": {"color": "goldenrod", "size": 7},
         "Венера": {"color": "khaki", "size": 15}, "Земля": {"color": "lightgreen", "size": 10},
         "Марс": {"color": "IndianRed1", "size": 5},  "Юпитер": {"color": "coral", "size": 20},
         "Сатурн": {"color": "DarkGoldenrod", "size": 19}, "Уран": {"color": "DeepSkyBlue", "size": 15},
         "Нептун": {"color": "CornflowerBlue","size": 14}, "Плутон": {"color": "Darkorange", "size": 5}}
for key, value in planet.items():
    y -= value["size"] * size1
    x += value["size"] * size1
    turtle.up()
    turtle.goto(x, y)
    turtle.down()
    turtle.fillcolor(value["color"])
    turtle.begin_fill()
    turtle.circle(value["size"] * size1)
    turtle.end_fill()
    if key == "Сатурн":  # рисуем кольца если Сатурн
        turtle.up()
        turtle.goto(x, y + ((value["size"] * size1) / 2))
        turtle.down()
        a = 50
        b = 20
        dx = turtle.xcor()
        dy = turtle.ycor()
        for deg in range(361):
            rad = math.radians(deg)
            x1 = a * math.sin(rad) + dx
            y2 = -b * math.cos(rad) + b + dy
            turtle.goto(x1, y2)
    turtle.up()
    turtle.goto(x, - value["size"] * size1 - 30)
    turtle.down()
    turtle.write(key, align="center", font=('Times New Roman', 12, 'normal'))
    x += (value["size"] * size1) + 20
    y = 0
turtle.done()
