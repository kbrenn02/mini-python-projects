from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    # The ball needs to move on it's own. So it takes the position it's currently at (self.xcor() - a built in call)
    # and updates it with the values above for moving. To make the ball move differently, change the x_move/y_move values
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    # If the ball hits the top or bottom wall, reverse the y direction (to actually account for the bounce)
    def wall_bounce(self):
        self.y_move *= -1

    # Same for the wall bounce but for the x (as if it was hitting the left or right walls)
    def paddle_bounce(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    # When a new round starts after a point was scored, start the ball at the initial position
    def reset_position(self):
        self.goto(0, 0)
        self.paddle_bounce()
        self.move_speed = 0.1
