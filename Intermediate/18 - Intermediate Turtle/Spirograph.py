from turtle import Turtle, Screen, colormode
from random import randint


def random_colors():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return r, g, b


t = Turtle()
t.speed('fastest')
colormode(255)
position = 1

for _ in range(360):
    t.color(random_colors())
    t.circle(100)
    t.setheading(_ * 2)





screen = Screen()
screen.exitonclick()
