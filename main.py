from turtle import Screen
from field import Field
from score import ScoreBoard
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.setup(width=1200, height=600)
screen.bgcolor("black")
screen.title("Let's play PONG !!!")
screen.tracer(False)
field = Field()
r_score = ScoreBoard((100, 260))
l_score = ScoreBoard((-110, 260))
r_paddle = Paddle((570, 0))
l_paddle = Paddle((-580, 0))
screen.listen()

screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")

screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

ball = Ball()

game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()
    if ball.distance(r_paddle) < 75 and ball.xcor() > 550 or ball.distance(l_paddle) < 75 and ball.xcor() < -550:
        ball.service()
    if ball.xcor() < -600:
        r_score.increase_score()
        ball.refresh_ball()
    if ball.xcor() > 600:
        l_score.increase_score()
        ball.refresh_ball()
    if l_score.score == 10 or r_score.score == 10:
        game_on = False
        game = ScoreBoard((0, 0))
        game.game_over()

screen.exitonclick()
