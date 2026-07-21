import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.turtle = Turtle()
        self.turtle.color(random.choice(COLORS))
        self.turtle.shape("square")
        self.turtle.penup()
        self.turtle.goto(300, random.randint(-250, 250))
        self.turtle.shapesize(1, 3)

    def move(self):
        self.turtle.goto(self.turtle.xcor()-STARTING_MOVE_DISTANCE,self.turtle.ycor())

    def position(self):
        return self.turtle.position()

    def increase_speed(self):
        global STARTING_MOVE_DISTANCE
        STARTING_MOVE_DISTANCE += MOVE_INCREMENT*0.1

    pass
