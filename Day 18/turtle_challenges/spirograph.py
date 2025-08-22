from turtle import Turtle, Screen
import random
t = Screen()
timmy = Turtle()
t.colormode(255)

timmy.speed(100)
heading = 5
gap = int(360 / heading)

for _ in range(gap):
    R = random.randint(0, 255)
    B = random.randint(0, 255)
    G = random.randint(0, 255)

    timmy.color((R, B, G))

    timmy.circle(100)
    timmy.setheading(timmy.heading() + heading)



t.exitonclick()
