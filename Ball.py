from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.penup()
        self.move_x = 10
        self.move_y = 10

    def move(self):
        current_x = self.xcor()
        current_y = self.ycor()
        new_x = current_x + self.move_x
        new_y = current_y + self.move_y
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.move_y *= -1

    def bounce_x(self):
        self.move_x *= -1

    def reset_position(self):
        self.goto(0, 0)
        self.bounce_x()
