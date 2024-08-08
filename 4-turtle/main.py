
# Types of imports
# 1. import turtle (this means every time you call on it, you have to type turtle.Turtle or turtle.Screen
# 2. from turtle import Turtle (this way you are calling in just one class written as x = Turtle()
# 3. from turtle import * (this imports every class and can make code confusing. Don't do this)
# 4. import turtle as t (this is alias, and allows you to shorten the name of potentially long imports)
        # this will look like the first thing, but shorted: t.Turtle() or t.Screen


import random
import turtle
# Need to pull specifically the Turtle and Screen classes from the turtle library
from turtle import Turtle, Screen

# Initiate the first turtle. Choose its color, shape, pensize, and speed
tim = Turtle()
turtle.colormode((255))
tim.shape("turtle")
directions = [0, 90, 180, 270]
tim.pensize(1)
tim.speed("fastest")


# To get the turtle to do anything but exist we should create some functions. Random color generator!
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

def draw_spirograph(size_of_gap):
    # The _ means that the loop variable is not needed, and will just run this 360/X times
    for _ in range(int(360/size_of_gap)):
        # Call the random_color function. Circle(x) is the radius of the circle. Setheading is the way the turtle is facing
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)

# Call the function
draw_spirograph(10)


# This shows the screen and doesn't let the screen disappear until it's clicked. This is really important to have when
# using the turtle library
screen = Screen()
screen.exitonclick()