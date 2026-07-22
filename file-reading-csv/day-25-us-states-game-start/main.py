import turtle
import pandas as pd

screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.bgpic("blank_states_img.gif")
screen.title("U.S. States Game")

def read_data():
    return pd.read_csv("50_states.csv")

df = read_data()

state_data = dict(zip(df.state, zip(df.x, df.y)))

write = turtle.Turtle()
write.penup()
write.color("black")
write.hideturtle()

game_on = True
while game_on:
    answer = screen.textinput("a", "Enter the name of state:")
    if answer in state_data:
        write.goto(state_data[answer][0], state_data[answer][1])
        write.pendown()
        write.write(answer)
        write.penup()
        print (state_data[answer])

