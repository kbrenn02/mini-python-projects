from turtle import Turtle
# Define global variables
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]


class Snake:
    # create 3 turtles and position them next to each other. Should be white squares that don't overlap
    def __init__(self): # what happens when we initialize a new snake object
        self.turtles = []
        self.create_snake()
        self.head = self.turtles[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_turtle(position)

    def add_turtle(self, position):
        new_turtle = Turtle(shape="square")
        new_turtle.penup()
        new_turtle.color("white")
        new_turtle.goto(position)
        self.turtles.append(new_turtle)  # have to say self.turtles to actually pull the turtles list

    def reset(self):
        for turtle in self.turtles:
            turtle.goto(1000, 1000)
        self.turtles.clear()
        self.create_snake()
        self.head = self.turtles[0]

    def extend(self):
        self.add_turtle(self.turtles[-1].position())

    def move(self):
        for num in range(len(self.turtles)-1, 0, -1):  # this makes last segment go to middle segment's last position
            new_x = self.turtles[num - 1].xcor()  # so if the head of the snake turns, so will the body
            new_y = self.turtles[num - 1].ycor()
            self.turtles[num].goto(new_x, new_y)
            # in plain words, turtles[2] (the last turtle) takes the xcor and ycor of turtles[1], having the last segment 
            # move to the position of the middle and the middle segment move to the position of the first. After that replacement, 
            # then the head turtle moves forward
        self.head.forward(MOVE_DISTANCE)

    # Define the angle/direction of the turtle (because it always moves forward)
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)