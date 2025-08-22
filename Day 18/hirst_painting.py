# import colorgram
#
# rgb = []
#
# colors = colorgram.extract('hirst.jpg', 15)
#
# for colour in colors:
#     r = colour.rgb.r
#     g = colour.rgb.g
#     b = colour.rgb.b
#     extracted_color = (r,g,b)
#     rgb.append(extracted_color)
#
# print(rgb)

from turtle import Turtle, Screen
import random

t = Turtle()
screen = Screen()
screen.colormode(255)
color_list = [(200, 172, 111), (240, 247, 244), (154, 179, 195), (192, 162, 176), (152, 185, 174), (215, 204, 116), (210, 179, 195), (175, 188, 213), (162, 211, 187), (163, 202, 214), (188, 163, 54), (115, 121, 183)]

t.penup()
t.hideturtle()


def position(pos_y):
    x = -250
    return t.goto(x, pos_y)

y = -250
position(y)

counter = 10

for _ in range(100):
    t.dot(20, random.choice(color_list))
    t.fd(50)
    counter -= 1

    if counter == 0:
        y += 50
        position(y)
        counter += 10







screen.exitonclick()
