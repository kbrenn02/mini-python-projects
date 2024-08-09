from turtle import Turtle
# Define the global variables for ease of reuse
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


# Score inherits from the Turtle class
class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        # We save the high score in a data.txt file. This 'with open(file)' gives us the ability to read it
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", False, align = ALIGNMENT, font = FONT)

    # If a new high score is made, write it to the data.txt file
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()