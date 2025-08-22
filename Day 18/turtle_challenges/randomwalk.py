from turtle import Turtle, Screen
import random

R = 0
G = 0
B = 0

timmy = Screen()
timmy.colormode(255)

t = Turtle()

choice = ["right","left","forward","backward"]


def randomwalk(direction):
    t.width(15)
    t.speed(4)
    R = random.randint(0, 255)
    B = random.randint(0, 255)
    G = random.randint(0, 255)

    t.color((R, B, G))

    if direction == "right":
        t.right(90)
    elif direction == "left":
        t.left(90)
    elif direction == "forward":
        t.forward(30)
    else:
        t.backward(30)

while True:
    randomwalk(random.choice(choice))

timmy.exitonclick()
