# Make necessary imports
from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
# Define the dimensions of the screen
screen.setup(width=500, height=400)
# Capture user input on their guess of which turtle will win
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ").lower()
print(user_bet)

# Define the colors the race turtles can be and the starting y positions, as well as the turtle array we will loop 
# through for the race
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

# Initialize all turtles for the race. This can also be done for color in colors
for turtle_index in range(0, 6):
    new_turtle = Turtle(shape = "turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x = -230, y = y_positions[turtle_index])
    # This adds the new turtle to the all_turtles array
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    # for every turtle, one at a time
    for turtle in all_turtles:
        # checking that the turtle hasn't already won. If it has, check if the winning turtle matches the user's bet
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
        # If there are no winners, the turtle moves forward a random number of pixels betwee 0 and 10.
        # Speed of fastest so the race looks smoother
        turtle.speed("fastest")
        random_distance = random.randint(0,10)
        turtle.forward(random_distance)


screen.exitonclick()