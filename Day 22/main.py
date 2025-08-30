from turtle import Turtle, Screen
from paddle import *
from ball import Ball
from scoreboard import *
import time

game_is_on = True

#screen appearance
screen = Screen()
screen.title("The Pong Game")
screen.setup(800,600)
screen.bgcolor("black")

screen.tracer(0)

divider = Divider()
score = Scoreboard()
ball = Ball()


l_paddle = Paddle(-350,0)
r_paddle = Paddle(350,0)

screen.listen()
screen.onkeypress(l_paddle.up, "w")
screen.onkeypress(l_paddle.down, "s")

screen.onkeypress(r_paddle.up, "Up")
screen.onkeypress(r_paddle.down, "Down")


while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 335 or ball.distance(l_paddle) < 50 and ball.xcor() < -335:
        ball.move_speed *= 0.9
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.move_speed = 0.1
        ball.reset_position()
        score.l_point()

    if ball.xcor() < -380:
        ball.reset_position()
        ball.move_speed = 0.1
        score.r_point()

screen.exitonclick()
