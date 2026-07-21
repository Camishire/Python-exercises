from turtle import Turtle

FONT = ("Courier", 24, "normal")

class Scoreboard:
    def __init__(self):
        self.turtle = Turtle()
        self.turtle.hideturtle()
        self.turtle.color("black")


    def write_score(self, score):
        self.turtle.penup()
        self.turtle.goto(-250, 250)
        self.turtle.pendown()
        self.turtle.write(f"Level: {score}", font=FONT)

    def clear(self):
        self.turtle.clear()

    def game_over(self):
        self.turtle.penup()
        self.turtle.goto(-100, 0)
        self.turtle.pendown()
        self.turtle.write("Game Over", font=FONT)
    pass
