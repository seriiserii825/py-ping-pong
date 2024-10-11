from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position): 
        super().__init__()
        self.shape('square')
        self.penup()
        self.color('white')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(position)

    def go_up(self):
        y = self.ycor()
        y += 60
        self.sety(y)

    def go_down(self):
        y = self.ycor()
        y -= 60
        self.sety(y)
