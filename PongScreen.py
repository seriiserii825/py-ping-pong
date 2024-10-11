from turtle import Screen


class PongScreen():
    def __init__(self):
        self.screen = Screen()
        self.screen.title("Pong Game")
        self.screen.setup(width=600, height=400)
        self.screen.bgcolor("black")

        self.screen.exitonclick()
