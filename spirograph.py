import random
import turtle
from turtle import Turtle, Screen

import random

tim = Turtle()
screen = Screen()
tim.shape("turtle")
turtle.colormode(255)
tim.speed(100)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


def spirograph():
    for i in range(360):
        tim.color(random_color())
        tim.circle(100)
        tim.left(i)


spirograph()
screen.exitonclick()
