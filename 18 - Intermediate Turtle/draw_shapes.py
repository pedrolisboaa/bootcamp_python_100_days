
def draw_shapes(last_shape):
    from turtle import Turtle, Screen
    t = Turtle()

    for i in range(3, last_shape):
        t.pencolor(colors())
        for _ in range(i):
            t.forward(100)
            t.left(360 / i)

    Screen().exitonclick()


def colors():
    from random import choice
    many_colors = ['medium blue', 'red', 'green', 'black', 'orange red', 'medium violet red', 'gold', 'khaki', 'dark olive green']
    return choice(many_colors)



draw_shapes(11)
