from turtle import Turtle
import random

# Food class inherits from the Turtle class
class Food(Turtle):

    def __init__(self):
        # initialize the parent class, giving the food class access to all its attributes
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("green")
        self.speed("fastest")
        self.refresh()

    # when a new food is placed, it's at a random x and y coordinate in the game board
    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)