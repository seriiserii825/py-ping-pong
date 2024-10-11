from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        current_x = self.xcor()
        current_y = self.ycor()
        new_x = current_x + self.x_move
        new_y = current_y + self.y_move
        self.goto(new_x, new_y)
