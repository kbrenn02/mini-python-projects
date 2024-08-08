# Make the necessary imports
from turtle import Turtle, Screen

# Initialize the first turtle and the screen
tim = Turtle()
screen = Screen()

# Create simple functions for moving the turtle forward and back, and deciding the angle it's pointing
def forwards():
    tim.forward(10)
def backwards():
    tim.backward(10)
def angle_right():
    tim.right(5)
def angle_left():
    tim.left(5)
def clear_screen():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

# The speed of zero means that the turtle is not moving on its own, which we want if it's supposed to be dependent on human commands
tim.speed(0)

# Need to start a screen listener so the computer knows to look for key presses
screen.listen()
# The onkey method is built into the screen class. By hovering over onkey, we see that it takes two args: a key (to press)
# and a function (which is why we defined our functions above)
screen.onkey(key = "w", fun = forwards) # move forwards
screen.onkey(key = "s", fun = backwards) # move backwards
screen.onkey(key = "a", fun = angle_left) # angle left
screen.onkey(key = "d", fun = angle_right) # angle right
screen.onkey(key = "c", fun = clear_screen)

screen.exitonclick()