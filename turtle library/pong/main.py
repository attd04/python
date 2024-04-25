
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# screen setup
screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

# paddles and ball and scoreboard
paddle_r = Paddle(350, 0)
paddle_l = Paddle(-350, 0)
ball = Ball()
scoreboard = Scoreboard()

# move paddles
screen.listen()
screen.onkey(paddle_r.up, "Up")
screen.onkey(paddle_r.down, "Down")
screen.onkey(paddle_l.up, "w")
screen.onkey(paddle_l.down, "s")


game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # detect top / bottom wall collision
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detect side wall collision + add points
    if ball.xcor() > 380:
        ball.reset()
        scoreboard.add_score_l()

    if ball.xcor() < -380:
        ball.reset()
        scoreboard.add_score_r()

    if scoreboard.score_r == 5 or scoreboard.score_l == 5:
        scoreboard.game_over()

    # collision w/ paddles
    if ball.distance(paddle_r) < 50 and ball.xcor() > 320:
        ball.bounce_x()

    if ball.distance(paddle_l) < 50 and ball.xcor() < -320:
        ball.bounce_x()


screen.exitonclick()



        
