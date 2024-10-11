from turtle import Screen
from Paddle import Paddle
from PongScreen import PongScreen

# pong_screen = PongScreen()

screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title('Pong Game')
screen.tracer(0)

l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))

screen.listen()
screen.onkey(l_paddle.go_up, 'w')
screen.onkey(l_paddle.go_down, 's')
screen.onkey(r_paddle.go_up, 'Up')
screen.onkey(r_paddle.go_down, 'Down')

game_is_on = True
while game_is_on:
    screen.update()

screen.exitonclick()
