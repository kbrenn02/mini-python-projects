# Make all the necessary imports
from turtle import Screen
from player import Player
from scoreboard import Scoreboard
from car_manager import CarManager
import time
import random

# Initialize and set up the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# Initialize the player, car manager, and scoreboard
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

# Create the hook to listen for key presses
screen.listen()
screen.onkey(player.move, "Up")
speed = 0

# Play the game
game_is_on = True
while game_is_on:
    scoreboard.update_level()
    time.sleep(0.1)
    screen.update()
    car_manager.generate()
    car_manager.cars_move()

    # Detect collision with a car
    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()
    
    if player.cross_finish_line():
        scoreboard.level_up()
        car_manager.level_up()



screen.exitonclick()
