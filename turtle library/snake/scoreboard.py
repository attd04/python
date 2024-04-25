# ------------------ SCOREBOARD.PY ------------------------
from turtle import Turtle, Screen
screen = Screen()


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt", "a") as file:
            self.high_score = int(file.read())
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", False, "center", ("Courier", 24, "normal"))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", "w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.color("white")
    #     self.hideturtle()
    #     self.penup()
    #     self.goto(0, 0)
    #     self.write("GAME OVER.", False, "center", ("Courier", 24, "normal"))

    def increase(self):
        self.score += 1
        self.update_scoreboard()
        
