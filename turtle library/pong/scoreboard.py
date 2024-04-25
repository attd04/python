# scoreboard.py
from turtle import Turtle, Screen
from ball import Ball
screen = Screen()
ball = Ball()
ball.hideturtle()

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score_l = 0
        self.score_r = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 200)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"{self.score_l}   {self.score_r}", False, "center", ("Courier", 80, "normal"))

    def add_score_r(self):
        self.score_r += 1
        self.clear()
        self.update_scoreboard()

        if self.score_r == 3:
            self.game_over()

    def add_score_l(self):
        self.score_l += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        ball.hideturtle()
        ball.stop()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 0)
        self.write("GAME OVER.", False, "center", ("Courier", 40, "normal"))

