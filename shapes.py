
import random
import turtle
from turtle import Turtle, Screen


tim = Turtle()
screen = Screen()
tim.shape("turtle")
turtle.colormode(255)
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

def shape(num_of_sides):
    angle = 360 / num_of_sides
    for i in range(num_of_sides):
        tim.forward(100)
        tim.left(angle)


for sides_shapes_n in range(3, 11):
    tim.color(random_color())
    shape(sides_shapes_n)

screen.exitonclick()

