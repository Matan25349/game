from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
tim.shape("turtle")
tim.color("blue")

def move_backwards():
    tim.back(10)
def move_forwards():
    tim.forward(10)


def move_left():
    new_heading=tim.heading()+10
    tim.setheading(new_heading)
def move_right():
    new_heading=tim.heading()-10
    tim.setheading(new_heading)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(key="Up", fun=move_forwards)
screen.onkey(key="Left", fun=move_left)
screen.onkey(key="Right", fun=move_right)
screen.onkey(key="Down",fun=move_backwards)
screen.onkey(key="c",fun=clear)
screen.exitonclick()