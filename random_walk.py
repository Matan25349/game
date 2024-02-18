import random
import turtle
from turtle import Turtle, Screen

import random

tim = Turtle()
screen = Screen()
tim.shape("turtle")
tim.pensize(15)
turtle.colormode(255)
tim.speed(100)
walk = [0, 90, 180, 270]


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


def random_walk():
    for j in range(10):
        tim.color(random_color())
        tim.forward(30)
        tim.right(random.choice(walk))


for i in range(30):
    random_walk()

screen.exitonclick()
