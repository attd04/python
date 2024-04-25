#etch a sketch project

import turtle
from turtle import Turtle, Screen
tim = Turtle("turtle")

def move_forward():
    tim.forward(10)

def move_backward():
    tim.backward(10)

def counter_clock():
    tim.left(20)

def clockwise():
    tim.right(20)

def clear():
    tim.penup()
    tim.clear()
    tim.home()
    tim.pendown()

screen.listen()

screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(counter_clock, "a")
screen.onkey(clockwise, "d")
screen.onkey(clear, "c")

screen.exitonclick()
