import turtle as t
import random


t.colormode(255)
def random_colors():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b,


tim = t.Turtle(shape='circle')
tim.shapesize()
tim.pensize(12)

while True:
    tim.color(random_colors())
    tim.setheading(random.choice([0, 180, 270]))
    tim.forward(random.choice(list(range(50, 101))))

screen = t.Screen()
screen.exitonclick()
