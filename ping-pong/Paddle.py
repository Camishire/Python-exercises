from turtle import Turtle

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_len=1, stretch_wid=3)
        self.penup()

    def move_up(self):
        if self.ycor() < 250:
            self.goto(self.xcor(), self.ycor() + 20)

    def move_down(self):
        if self.ycor() > -250:
            self.goto(self.xcor(), self.ycor() - 20)