from turtle import Screen, Turtle
import time
import turtle
from Paddle import*
from Ball import*
from Wall import*

right_paddle_starting_pos=[380, 0]
left_paddle_starting_pos=[-380, 0]
ball_starting_pos=[380, 0]
score = [0,0]

screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.tracer(0)
screen.title('Ping Pong')

paddle_right=Paddle()
paddle_right.goto(right_paddle_starting_pos[0],right_paddle_starting_pos[1])
paddle_left=Paddle()
paddle_left.goto(left_paddle_starting_pos[0],left_paddle_starting_pos[1])

wall=Wall()
ball=Ball()

screen.listen()
screen.onkeypress(paddle_left.move_up, 'w')
screen.onkeypress(paddle_left.move_down, 's')
screen.onkeypress(paddle_right.move_up, 'Up')
screen.onkeypress(paddle_right.move_down, 'Down')

scores = Turtle()
scores.color('white')
scores.penup()
scores.hideturtle()
scores.goto(0, 220)

game = True
try:
    while game:
        screen.update()
        time.sleep(ball.move_speed)
        ball.move()
        ball.bounce_wall()
        scores.clear()
        scores.write(f"{score[0]} || {score[1]}", align='center', font=('Courier', 50, 'bold'))

        if ball.distance(paddle_right) < 50 and ball.xcor() > 320:
            ball.bounce_paddle()

        if ball.distance(paddle_left) < 50 and ball.xcor() < -320:
            ball.bounce_paddle()

        if ball.xcor() > 390:
            score[0] += 1
            ball.reset_position()

        if ball.xcor() < -390:
            score[1] += 1
            ball.reset_position()

        if score[0] == 3:
            print("Game Over. Left player wins!")
            game = False
        elif score[1] == 3:
            print("Game Over. Right player wins!")
            game = False

except turtle.Terminator:
    print("Window closed - exiting cleanly.")