import turtle
import random
xsize = 450
ysize = 450
zvzd_numb = 200  # кол-во звезд
turtle.Screen().bgcolor("DarkBlue")
turtle.hideturtle()
turtle.speed(0)
turtle.tracer(10, 5)
def ZVZD():
    zvezda = {"size": random.randrange(5, 10),
              "color": random.choice(["yellow3", "khaki", "magenta"]),
              "x": random.randrange(-xsize, xsize), "y": random.randrange(0, ysize)}
    turtle.up()
    turtle.goto(zvezda["x"], zvezda["y"])
    turtle.down()
    turtle.pensize()
    turtle.dot(zvezda["size"], zvezda["color"])

def ZdaN():

    # определяем размер и кол-во домов
    total = 0
    X_X = xsize * 2
    small_size_x = X_X / 16
    medium_size_x = X_X / 8
    large_size_x = X_X / 4
    while(total < X_X or total > X_X):
        zdan = {"small_numb": random.randrange(1, 16), "medium_numb": random.randrange(1, 8),
                "large_numb": random.randrange(1, 4)}
        total = zdan["small_numb"] * small_size_x + zdan["medium_numb"] * medium_size_x + \
                zdan["large_numb"] * large_size_x
    print(total)
    Y_Y = (ysize * 2) - ((ysize * 2) / 5)
    smal_size_y = Y_Y - (ysize / 2) -100
    midium_size_y = Y_Y - (ysize / 4)
    large_size_y = Y_Y
    bild = {"small": {"numb": zdan["small_numb"], "b_x": small_size_x, "b_y": smal_size_y, "win": 3 },
            "medium": {"numb": zdan["medium_numb"], "b_x": medium_size_x, "b_y": midium_size_y, "win": 5},
            "large": {"numb": zdan["large_numb"], "b_x": large_size_x, "b_y": large_size_y, "win": 7}}
    turtle.up()
    turtle.goto(-xsize, -ysize)
    turtle.down()
    turtle.left(90)
    # рисуем здания
    while(bild["small"]["numb"] + bild["medium"]["numb"] + bild["large"]["numb"] != 0 ):
        start = random.choice(["small", "medium", "large"])
        while(bild[start]["numb"] == 0):
            start = random.choice(["small", "medium", "large"])
        turtle.fillcolor("Blue")
        turtle.pencolor("Blue")
        turtle.begin_fill()
        for i in range(4):
            if i % 2 == 0:
                turtle.fd(bild[start]["b_y"])
            else:
                turtle.fd(bild[start]["b_x"])
            turtle.right(90)
        turtle.end_fill()
        turtle.right(90)

        # делаем окна рисуем каркас
        delt = 0
        total = 0
        delt = bild[start]["b_x"] / bild[start]["win"]
        x_win, y_win = 0, 0
        turtle.fd(delt)
        turtle.left(90)
        while (y_win < bild[start]["b_y"]):
            for w in range(bild[start]["win"] - 2):
                if random.randrange(10) % 3 == 0:  # определяем какие окна будут гореть
                    if random.randrange(2) == 1:
                        turtle.fillcolor("yellow")
                        turtle.begin_fill()
                        for wi in range(4):
                            turtle.fd(delt)
                            turtle.right(90)
                        turtle.end_fill()
                else:
                    for wi in range(4):
                        turtle.fd(delt)
                        turtle.right(90)
                turtle.right(90)
                turtle.fd(delt)
                turtle.left(90)

            y_win += delt
            turtle.left(90)
            turtle.fd(delt * (bild[start]["win"] - 2))
            turtle.right(90)
            total += 1
            if y_win + delt < bild[start]["b_y"]:
                turtle.fd(delt)

        turtle.bk((total - 2) * delt)
        turtle.right(90)
        turtle.fd((bild[start]["win"] - 1) * delt)
        #turtle.fd(bild[start]["b_x"])
        turtle.left(90)

        bild[start]["numb"] -= 1

for i in range(random.randrange(30, zvzd_numb)):
    ZVZD()
ZdaN()

turtle.done()