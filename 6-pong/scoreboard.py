# Allow user to create turtle graphics
from turtle import Turtle

# This indicates that Scoreboard inherits from Turtle, giving it access to all methods and attributes of a "Turtle"
# The idea is to show a scoreboard using turtle graphics
class Scoreboard(Turtle):

    def __init__(self):
        # super().__init__() is similar to def __init__. It calls the initializer of the parent class Turtle,
        # ensuring that the class is properly initialized before adding custom behavior in the Scoreboard class
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        # clear the score that is present so it can be updated
        self.clear()
        self.goto(-100, 200)
        # Note that l_point and r_point both call update scoreboard after increasing self.l_score and self.r_score, respectively
        # This part here is what actually updates the scoreboard score
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))

    # Methods for giving points to each side
    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()

    def game_over(self):
        if self.r_score == 3:
            self.goto(0, 0)
            self.write("Right Player Wins!", align="center", font=("Courier", 40, "normal"))
        elif self.l_score == 3:
            self.goto(0, 0)
            self.write("Left Player Wins!", align="center", font=("Courier", 40, "normal"))