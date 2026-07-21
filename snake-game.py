from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=635, height=635)
screen.bgcolor('black')
screen.tracer(0)

snake = Turtle()
snake.color('green')
snake.shape('arrow')
snake.width(5)
snake.speed(0)
snake.penup()

segments = []

fruit = Turtle()
fruit.color('red')
fruit.shape('circle')
fruit.shapesize(0.5)
fruit.penup()

angle = 90
length = 10
score = 0

def turn_right():
    snake.right(angle)

def turn_left():
    snake.left(angle)

def place_fruit():
    random_x = random.randint(-290, 290)
    random_y = random.randint(-290, 290)
    fruit.goto(random_x, random_y)

def add_segment():
    new_segment = Turtle()
    new_segment.color('lightgreen')
    new_segment.shape('square')
    new_segment.shapesize(0.4)
    new_segment.penup()
    new_segment.goto(snake.position())
    segments.append(new_segment)

place_fruit()

def game_loop():
    global score
    if -300 < snake.xcor() < 300 and -300 < snake.ycor() < 300:
        for i in range(len(segments) - 1, 0, -1):
            segments[i].goto(segments[i - 1].position())
        if segments:
            segments[0].goto(snake.position())

        snake.forward(length)

        if snake.distance(fruit) < 15:
            score += 1
            print("Score:", score)
            place_fruit()
            add_segment()

        screen.update()
        screen.ontimer(game_loop, 100)
    else:
        print("Game over! Final score:", score)

screen.listen()
screen.onkey(turn_right, 'd')
screen.onkey(turn_left, 'a')

game_loop()
screen.mainloop()