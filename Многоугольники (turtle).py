import turtle
import random
import math
flag = True
S = 50
a = float(0.0)
Sx, x0, y0, x1, y1 = 0, -350, 400, 0, 210
size = 15  # размер фигур
#turtle.hideturtle()  # начальное положение черепашки верхний левый угол
for row in range(5):
    turtle.up()
    turtle.goto(x0, y1)
    x1 = x0
    for colomn in range(5):
        #color = tuple(random.randrange(0, 255) for _ in "123")
        color = random.choice(['red', 'blue', 'yellow', 'black', 'orange', 'violet', 'gold', 'cyan', 'grey', 'pink', 'khaki', 'lawngreen', 'hotpink', 'lightblue', 'lightgrey', 'magenta'])
        n = random.choice([3, 4, 6, 7])
        while (flag == True):  # определяем длину сторон в зависимости от кол-ва сторон и заданной плащади
            Sx = ((n * (a ** 2)) / (4 * math.tan(math.radians(180) / n)))
            a += 0.1
            if (Sx <= S and Sx >= S - 0.5) or (Sx >= S and Sx <= S + 0.5) or (Sx == S) or Sx > S:
                break
        #print(row, colomn, n, a, Sx)
        turtle.up()
        turtle.goto(x1, y1)

        # задаем смещение по оси х для квадрата и шестигранника
        if n == 4 or n == 6:
            x1 += ((a / 2) * size)
            turtle.left(180 - (180 - 360 / n))  # разварачиваем черепашку на старте
            turtle.goto(x1, y1)
        elif n == 3:
            turtle.left(180 - 360 / n)  # разварачиваем черепашку на старте
        elif n == 7:
            turtle.left((360 / n) / 2)  # разварачиваем черепашку на старте

        turtle.down()  # рисуем саму фигуру
        turtle.fillcolor(color)
        turtle.begin_fill()
        for i in range(n):
            turtle.fd(a * size)
            turtle.left(360 / n)
        turtle.end_fill()

        turtle.setheading(0)  # возвращаем черепашку в исходное (стартовое положение)
        if n == 6 or n == 4:
            turtle.bk((a / 2) * size)
            turtle.up()
            x1 -= ((a / 2) * size)
        x1 += size + 150  # задание стартовой точки для следующей фигуры по оси Х
        a = 0
    y1 -= size + 180  # переход на новую строку