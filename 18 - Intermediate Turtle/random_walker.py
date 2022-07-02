from turtle import Turtle, Screen
from random import randint, choice

CORES = ['medium blue', 'red', 'green', 'black', 'orange red', 'medium violet red', 'gold', 'khaki', 'dark olive green']

t = Turtle(shape='circle')
t.shapesize()
t.pensize(12)
while True:
    t.pencolor(choice(CORES))
    t.setheading(choice([0, 180, 270]))
    t.forward(choice(list(range(50, 101))))








screen = Screen().exitonclick()
