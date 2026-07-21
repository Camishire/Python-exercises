import time
import turtle
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
FINISH_LINE_Y = 300

screen.listen()
screen.onkeypress(player.MoveForwards, "Up")

game_is_on = True
cars = []
increment = 0
level = 1
score = Scoreboard()

try:
    while game_is_on:
        time.sleep(0.1)
        increment += 1
        score.write_score(level)

        if increment == 6:
            car = CarManager()
            cars.append(car)
            increment = 0

        for car in cars[:]:
            car.move()
            pos = car.position()
            if pos[0] < -350:
                cars.remove(car)
            if car.turtle.distance(player.turtle) < 20:
                score.game_over()
                game_is_on = False
            if player.turtle.distance(0, FINISH_LINE_Y) < 20:
                level += 1
                score.clear()
                player.turtle.goto(0, -280)
                for c in cars[:]:
                    c.increase_speed()

        screen.update()

except (turtle.Terminator, turtle._tkinter.TclError):
    print("Window closed - exiting cleanly.")

screen.exitonclick()