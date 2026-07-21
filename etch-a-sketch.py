from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
angle = 10
length = 10

def move_forwards():
    tim.forward(length)

def move_backwards():
    tim.backward(length)

def turn_right():
    tim.right(angle)

def turn_left():
    tim.left(angle)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(move_forwards, 'w')
screen.onkey(move_backwards, 's')
screen.onkey(turn_right, 'd')
screen.onkey(turn_left, 's')
screen.onkey(clear, 'c')

screen.exitonclick()
