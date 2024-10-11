import time
from turtle import Screen

import screeninfo

from Ball import Ball
from Paddle import Paddle
from ScoreBoard import ScoreBoard

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

monitor = screeninfo.get_monitors()[0]
monitor_width = monitor.width
monitor_height = monitor.height
start_x = monitor_width // 2 - SCREEN_WIDTH // 2
start_y = monitor_height // 2 - SCREEN_HEIGHT // 2

screen = Screen()
screen.bgcolor('black')
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT, startx=start_x, starty=start_y)
screen.title('Pong Game')
screen.tracer(0)

l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))

screen.listen()
screen.onkey(l_paddle.go_up, 'd')
screen.onkey(l_paddle.go_down, 'f')
screen.onkey(r_paddle.go_up, 'Up')
screen.onkey(r_paddle.go_down, 'Down')

ball = Ball()
ball.move()

scoreboard = ScoreBoard(SCREEN_WIDTH, SCREEN_HEIGHT)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    ball.move()

    # Detect collision with wall
    if ball.ycor() > SCREEN_HEIGHT // 2 - 20 or ball.ycor() < -SCREEN_HEIGHT // 2 + 20:
        ball.bounce_y()
        
    # Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    else:
        if ball.xcor() > SCREEN_WIDTH // 2:
            ball.reset_position()
            scoreboard.l_scored()

        if ball.xcor() < -SCREEN_WIDTH // 2:
            ball.reset_position()
            scoreboard.r_scored()

screen.exitonclick()
