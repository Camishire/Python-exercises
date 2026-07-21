from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player:
    def __init__(self):
        self.turtle = Turtle()
        self.move_speed = MOVE_DISTANCE
        self.turtle.penup()
        self.turtle.left(90)
        self.turtle.shape("turtle")
        self.turtle.color("black")
        self.turtle.goto(STARTING_POSITION)

    def MoveForwards(self):
        self.turtle.forward(MOVE_DISTANCE)

    def Position(self):
        return self.turtle.position()

    pass
