from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


# Create global, unchanging variables for the starting positions of the paddles
STARTING_POSITION_RIGHT = (350, 0)
STARTING_POSITION_LEFT = (-350, 0)

# Initialize the screen and give it the aesthetics of the game
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

# Initialize the paddles, ball, and scoreboard
right_paddle = Paddle(STARTING_POSITION_RIGHT)
left_paddle = Paddle(STARTING_POSITION_LEFT)
ball = Ball()
scoreboard = Scoreboard()

# create a listener hook so the program knows to look for key presses
screen.listen()
# move right paddle
screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")

# move left paddle
screen.onkey(left_paddle.up, "w")
screen.onkey(left_paddle.down, "s")

game_is_on = True
while game_is_on:
    scoreboard.update_scoreboard()
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    # ball.paddle_bounce()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.wall_bounce()

    # detect collision with paddles
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor()< -320:
        ball.paddle_bounce()

    # right paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # left paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

    if scoreboard.l_score == 3:
        game_is_on = False
    
    if scoreboard.r_score == 3:
        game_is_on = False

scoreboard.game_over() 

screen.exitonclick()