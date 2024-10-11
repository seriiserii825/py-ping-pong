from turtle import Screen, Turtle
from PongScreen import PongScreen

# pong_screen = PongScreen()

screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title('Pong Game')
screen.tracer(0)

paddle = Turtle()
paddle.shape('square')
paddle.penup()
paddle.color('white')
paddle.shapesize(stretch_wid=5, stretch_len=1)
paddle.goto(350, 0)

def go_up():
    y = paddle.ycor()
    y += 20
    paddle.sety(y)

def go_down():
    y = paddle.ycor()
    y -= 20
    paddle.sety(y)

screen.listen()
screen.onkey(go_up, 'Up')
screen.onkey(go_down, 'Down')

game_is_on = True
while game_is_on:
    screen.update()

screen.exitonclick()
