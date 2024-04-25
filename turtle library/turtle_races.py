import turtle
from turtle import Turtle, Screen

screen = Screen()

# turtle race
import random
is_race_on = False

screen.setup(500, 400)
guess = turtle.textinput("Make your bet!", "Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_position = [-100, -50, 0, 50, 100, 150]
all_turtles = []

for turtle_index in range(0, 6):
    tim = Turtle("turtle")
    tim.penup()
    tim.goto(-230, y_position[turtle_index])
    tim.color(colors[turtle_index])
    all_turtles.append(tim)

if guess:
    is_race_on = True


while is_race_on:

    for turtle in all_turtles:

        if turtle.xcor() > 230:
            is_race_on = False
            winner = turtle.pencolor()

            if winner == guess:
                print(f"You win! The {winner} turtle is the winner!")

            else:
                print(f"You lose. The {winner} turtle won.")

        distance = random.randint(0, 10)
        turtle.forward(distance)

screen.exitonclick()
