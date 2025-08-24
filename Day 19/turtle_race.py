from turtle import Turtle, Screen
import random

race_is_on = False
screen = Screen()
screen.setup(500,400)

user_bet = screen.textinput("Make your bet", "Which turtle will win the race? Enter a color").lower()

if user_bet:
    race_is_on = True

directions = [-70, -40, -10, 20, 50, 80]
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
new_turtles = []

for turtle in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle])
    new_turtle.goto(x=-230, y=directions[turtle])
    new_turtles.append(new_turtle)

while race_is_on:
    for turtle in new_turtles:
        turtle.forward(random.randint(0, 10))
        if turtle.xcor() > 230:
            race_is_on = False
            if turtle.color == user_bet:
                print(f"You won! {turtle.pencolor()} won the race")
            else:
                print(f"You lose. {turtle.pencolor()} won the race")

screen.exitonclick()
