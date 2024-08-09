from turtle import Turtle
FONT = ("Courier", 24, "normal")

# Keeping score with turtles, as I have with the past several games
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__() # inherit all attributes from the Turtle class
        self.color("black")
        self.penup()
        self.hideturtle()
        self.level = 1
        self.update_level()

    def update_level(self):
        self.clear()
        self.goto(-240, 260)
        self.write(f"Level {self.level}", align="center", font=FONT)

    def level_up(self):
        self.level += 1
        self.update_level()

    def game_over(self):
        self.hideturtle()
        self.goto(0, 0)
        self.write("Game over", align="center", font=FONT)
