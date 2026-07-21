from turtle import Turtle, Screen
import random

colors = ['purple', 'blue', 'green', 'yellow', 'orange', 'red']
names = ['Mike', 'Tyson', 'Lady', 'Gaga', 'Sabrina', 'Carpenter']

def create_turtle(color):
    t = Turtle()
    t.shape('turtle')
    t.color(color)
    t.speed(5)
    return t

def move_to_starting_position(y, turtle):
    turtle.penup()
    turtle.goto(-400, y)
    turtle.pendown()

def move_at_random(turtle):
    turtle.forward(random.randint(0, 10))

screen = Screen()
screen.setup(width=900, height=500)

chosen_color=screen.textinput("Choise window.", "Enter the color of turtle:")

turtles = []
y = 200
for i, name in enumerate(names):
    t = create_turtle(colors[i])
    move_to_starting_position(y, t)
    turtles.append((name, t))
    y -= 50

winner = None
while winner is None:
    for name, t in turtles:
        move_at_random(t)
        if t.xcor() > 400:
            winner = (name, t.color()[0])
            break

print(f"Winning turtle: {winner[0]}, color: {winner[1]}")
if winner[1] == chosen_color:
    print("You win!")
else:
    print("You lose!")

screen.exitonclick()