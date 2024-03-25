# BALL BOUNCE GAME
# paddle at base, moves right & left, if miss then life -1, 3 chances, score +1

import turtle
import os

# GAME WINDOW
window = turtle.Screen()
window.title("Ball Bounce by Gaurav")
window.bgcolor("black")
window.setup(width=600, height=400)
window.tracer(0)

turtle.textinput("New Game", "Click OK to start game")

# PADDLE
paddle = turtle.Turtle()
paddle.speed(0)
paddle.shape("square")
paddle.shapesize(stretch_len=5, stretch_wid=1)
paddle.color("blue")
paddle.penup()
paddle.goto(0, -150)

# BALL
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("yellow")
ball.penup()
ball.goto(0, 0)
ball.dx = 2
ball.dy = 2

# SCORE
score = turtle.Turtle()
score.speed(0)
score.color("red")
score.hideturtle()
score.penup()
score.goto(200, 160)
score.write("Score: 0", align="center", font=("Courier", 20, "normal"))

# LIFE
life = turtle.Turtle()
life.speed(0)
life.color("red")
life.hideturtle()
life.penup()
life.goto(-240, 160)
life.write("Life: 3", align="center", font=("Courier", 20, "normal"))

# FUNCTION


def paddle_right():
    x = paddle.xcor()
    x += 20
    paddle.setx(x)


def paddle_left():
    x = paddle.xcor()
    x -= 20
    paddle.setx(x)


# KEYBOARD BINDING
window.listen()
window.onkeypress(paddle_right, "Right")
window.onkeypress(paddle_left, "Left")

# Score_game & Life_game
score_game = 0
life_game = 3

# MAIN GAME LOOP
while True:
    window.update()

    # MOVE THE BALL
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # BORDER CHECKING
    if ball.ycor() > 185:  # top border
        ball.sety(185)
        ball.dy *= -1

    if ball.ycor() < -185:  # lower border
        ball.goto(0, 0)
        ball.dy *= -1
        os.system("afplay dishbreaking.wav&")
        life_game -= 1
        life.clear()
        life.write(f"Life: {life_game}", align="center",
                   font=("Courier", 20, "normal"))

    if ball.xcor() > 285:  # right border
        ball.setx(285)
        ball.dx *= -1

    if ball.xcor() < -285:  # left border
        ball.setx(-285)
        ball.dx *= -1

    # PADDLE & BALL COLLISION
    if (ball.ycor() > -150 and ball.ycor() < -130) and (ball.xcor() < paddle.xcor() + 50 and ball.xcor() > paddle.xcor() - 50):
        ball.sety(-130)
        ball.dy *= -1
        score_game += 1
        os.system("afplay spring.wav&")
        score.clear()
        score.write(f"Score: {score_game}", align="center",
                    font=("Courier", 20, "normal"))

    # GAME OVER CONDITION
    if life_game == 0:
        life.clear()
        score.clear()
        life.goto(0, 0)
        life.write(
            f"You lost all your lives. GAME OVER. Your score was {score_game}", align="center", font=("Courier", 16, "normal"))
        os.system("afplay ahh.wav&")
        turtle.done()
