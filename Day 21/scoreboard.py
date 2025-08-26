from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Courier', 12, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.gamescore = 0
        self.color("White")
        self.penup()
        self.goto(0,275)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.gamescore}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
    def increase_score(self):
        self.clear()
        self.gamescore += 1
        self.update_scoreboard()
