from turtle import Turtle, Screen


############### FUNCTIONS ########################
def square(tartaruginha):
    for _ in range(4):
        tartaruginha.forward(200)
        tartaruginha.right(90)


def draw(t):
    for _ in range(10):
        t.forward(10)
        t.penup()
        t.forward(10)
        t.pendown()



if __name__ == '__main__':

    tartaruga = Turtle(shape='circle')
    tartaruga.color('green')

    #square(tartaruga)
    draw(tartaruga)

    screen = Screen().exitonclick()
