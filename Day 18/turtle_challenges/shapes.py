from turtle import Turtle, Screen
import random

R = 0
G = 0
B = 0

timmy = Screen()
timmy.colormode(255)

t = Turtle()

number_of_sides = 3

while number_of_sides != 10:
    R = random.randint(0, 255)
    B = random.randint(0, 255)
    G = random.randint(0, 255)
    angle = 360 / number_of_sides
    for i in range(number_of_sides):
        t.pencolor((R, B, G))
        t.right(angle)
        t.forward(100)

    number_of_sides += 1


timmy.exitonclick()


