from turtle import Turtle, Screen, colormode
from random import randint


def random_colors():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return r, g, b


colormode(255)
t = Turtle()
t.hideturtle()
t.speed('fastest')
t.penup()
t.setheading(225)
t.forward(300)
t.setheading(0)

number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    t.dot(20, random_colors())
    t.forward(50)

    if dot_count % 10 == 0:
        t.setheading(90)
        t.forward(50)
        t.setheading(180)
        t.forward(500)
        t.setheading(0)






screen = Screen()
screen.exitonclick()