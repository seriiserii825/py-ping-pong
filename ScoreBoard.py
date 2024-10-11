from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self, screen_width, screen_height):
        super().__init__()
        self.SCREEN_WIDTH = screen_width
        self.SCREEN_HEIGHT = screen_height
        self.color('white')
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.write(f'{self.l_score}   {self.r_score}', align='center', font=('Courier', 80, 'normal'))
        print(self.SCREEN_HEIGHT)
        self.goto(0, self.SCREEN_HEIGHT // 2 * -1)
