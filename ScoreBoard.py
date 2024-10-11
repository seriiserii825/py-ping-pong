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
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f'{self.l_score}   {self.r_score}', align='center', font=('Courier', 80, 'normal'))
        self.goto(20, 20)

    def l_scored(self):
        self.l_score += 1
        self.update_score()

    def r_scored(self):
        self.r_score += 1
        self.update_score()
