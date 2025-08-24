from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(10)
def move_backward():
    tim.backward(10)

def move_upward():
    heading = tim.heading() + 10
    tim.setheading(heading)
def move_downward():
    heading = tim.heading() - 10
    tim.setheading(heading)
def clear():
    tim.reset()



screen.listen()
screen.onkeypress(key="w", fun=move_upward)
screen.onkeypress(key="d", fun=move_forward)
screen.onkeypress(key="a", fun=move_backward)
screen.onkeypress(key="s", fun=move_downward)
screen.onkeypress(key="c", fun=clear)

screen.exitonclick()
