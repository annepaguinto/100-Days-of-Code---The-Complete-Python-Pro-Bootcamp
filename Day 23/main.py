import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

score = Scoreboard()
car_manager = CarManager()
player = Player()

screen.listen()
screen.onkeypress(player.move, "Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    score.display_score()

    car_manager.create_car()
    car_manager.move_cars()


    for car in car_manager.cars:
        if car.distance(player) < 20:
            score.game_over()
            game_is_on = False

    if player.ycor() > player.finishline:
        score.increase_score()
        car_manager.level_up()
        player.start()

screen.exitonclick()
