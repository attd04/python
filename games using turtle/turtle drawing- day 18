from turtle import Turtle, Screen
import colorgram
import turtle as t
import random

tim = Turtle()
tim.shape("turtle")
tim.color("darkgreen", "lightgreen")

# different shapes overlapping kinda
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'violet', 'purple', 'pink']

def shapes(n_sides):
    angle = 360 / n_sides
    for _ in range(n_sides):
        tim.forward(100)
        tim.right(angle)

for shape_sides in range (3, 11):
    tim.pencolor(random.choice(colors))
    shapes(shape_sides)
# -----------------------------

# random walk with random colors
t.colormode(255)
directions = [0, 90, 180, 270]
tim.pensize(4)
tim.speed(9)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color = (r, g, b)
    return color

for _ in range (150):
    tim.pencolor(random_color())
    tim.forward(25)
    tim.setheading(random.choice(directions))

# ------------------------------------

# spirograph
tim.speed(0)
t.colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color = (r, g, b)
    return color

for _ in range (100):
    tim.pencolor(random_color())
    tim.circle(100)
    tim.right(3.6)

# ------------------------------------

# random colored dots spaced in square shape

def getting_colors():
    rgb_colors = []
    colors = colorgram.extract('colros.jpg', 9)

    for color in colors:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        new_color = (r,g,b)
        rgb_colors.append(color.rgb)

color_list = [(245, 216, 195), (190, 212, 223), (248, 129, 97), (252, 185, 88), (18, 99, 122), (187, 84, 84), (0, 60, 77), (0, 0, 0), (85, 198, 230)]

t.colormode(255)
tim.speed(0)
tim.penup()

position_x = -250
position_y = -200

for _ in range (10):
    tim.goto(position_x, position_y)
    position_y += 50
    for _ in range (10):
        tim.dot(20, random.choice(color_list))
        tim.forward(50)

screen = Screen()
screen.exitonclick()
