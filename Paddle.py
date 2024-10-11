from turtle import Turtle


class Paddle():
    def __init__(self): 
       self.paddle = Turtle()
       self.paddle.shape('square')
       self.paddle.color('white')
       self.paddle.turtlesize(20, 100)
       self.paddle.setposition(350, 0)
