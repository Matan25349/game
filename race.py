from turtle import Turtle, Screen
import random

is_race_on = False

screen = Screen()
screen.setup(500, 400)
usr_bet = screen.textinput(title="make your bet", prompt="enter a color")
print(usr_bet)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-100, -70, -40, -10, 20, 50]
all_turtles = []
for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(-230, y_positions[turtle_index])
    all_turtles.append(new_turtle)

if usr_bet:
    is_race_on = True

while is_race_on:
    for i in all_turtles:
        if i.xcor() > 230:
            is_race_on=False
            winning_color=i.pencolor()
            if winning_color==usr_bet:

                print(f"the {winning_color} won!")
            else:
                print(f"you lost, the {winning_color} Won!")

        rand_distance = random.randint(0, 10)
        i.forward(rand_distance)

screen.exitonclick()
