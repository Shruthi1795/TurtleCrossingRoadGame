from turtle import Screen
from car_manager import CarManager
from player import Player
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.go_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()
    scoreboard.update_scoreboard()

    # Detect collision with Cars
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    # Detect the turtle on other end
    if player.finish():
        player.go_to_start()
        scoreboard.update_score()
        car_manager.increase_speed()

screen.exitonclick()
