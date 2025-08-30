from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, x_cor, y_cor):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.penup()
        self.x_cor = x_cor
        self.y_cor = y_cor
        self.goto(x_cor, y_cor)

    def up(self):
        self.y_cor = self.ycor() + 20
        self.goto(self.x_cor,self.y_cor)


    def down(self):
        self.y_cor = self.ycor() - 20
        self.goto(self.x_cor,self.y_cor)

        
class Divider(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")

        self.penup()
        self.hideturtle()
        self.pensize(3)
        self.goto(0, 295)

        for _ in range(29):
            self.penup()
            self.forward(10)
            self.setheading(270)
            self.pendown()
            self.forward(10)
