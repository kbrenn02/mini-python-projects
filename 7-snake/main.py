from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Score
import time


# screen set up. Black background w/ title My Snake Game
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0) #turn turtle animation on/off and set delay for update drawings. So while off, nothing happens

# Initialize the snake, food, and scoreboard
snake = Snake()
food = Food()
scoreboard = Score()

# Add a screen listener so it knows to look for key presses
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


# animating snake segments on screen

game_is_on = True
while game_is_on:
    screen.update() # update screen after all turtles move
    time.sleep(0.1) # a 0.1 sec delay before moving turtles again
    snake.move()

    # detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
    
    # detect collision with the wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -295 or snake.head.ycor() > 295 or snake.head.ycor() < -280:
        snake.reset()
        scoreboard.reset()

    # detect collision with the tail
    for segment in snake.turtles[1:]: # for any segment except the head
        if snake.head.distance(segment) < 10:
            snake.reset()
            scoreboard.reset()



screen.exitonclick()