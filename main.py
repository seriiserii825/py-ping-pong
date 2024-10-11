import time
from turtle import Screen

import screeninfo

from Ball import Ball
from Paddle import Paddle

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

monitor = screeninfo.get_monitors()[0]
monitor_width = monitor.width
monitor_height = monitor.height
start_x = monitor_width // 2 - SCREEN_WIDTH // 2
start_y = monitor_height // 2 - SCREEN_HEIGHT // 2

# pong_screen = PongScreen()


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

count = 1

game_is_on = True
while game_is_on:
    screen.update()
    if count != 20:
        time.sleep(0.1)
        ball.move()
        count += 1

screen.exitonclick()
