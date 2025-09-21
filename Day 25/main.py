import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

answer = turtle.Turtle()

df_states = pandas.read_csv("50_states.csv")
states_list = df_states["state"].to_list()

score = 0
title = "Guess the state"

while score < 50:
    answer_state = screen.textinput(title=title, prompt="What's the state's name?").title()

    for state in states_list:
        if answer_state == state:
            score += 1
            states_list.remove(state)
            title = f"{score}/{len(states_list)} States Correct"
            matched_row = df_states[df_states["state"] == state]
            print()
            x = matched_row["x"].item()
            y = matched_row["y"].item()
            answer.hideturtle()
            answer.penup()
            answer.goto(x, y)
            answer.write(state)

    if answer_state == "Exit":
        df_to_learn = pandas.DataFrame(states_list)
        df_to_learn.to_csv("states_to_learn.csv")
        break

