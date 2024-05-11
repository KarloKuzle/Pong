from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
# set ball speed to 1px or import time and put time.sleep(0.1) in the game loop
import time

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("My Pong Game")
screen.tracer(0)


# when you turn off the animation you have to manually update the screen

# paddle info
# width = 20
# height = 100
# x_pos = 350
# y_pos = 0
# all turtles start off by 20x20
# ball -> 20x20 px

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with r_paddle
    # since the paddle isn't a circular nor symmetrical object
    # we have to set a vertical line trigger for to also detect the ball
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect when paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()