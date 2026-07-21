from turtle import Turtle

class Wall(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_len=0.1, stretch_wid=50)