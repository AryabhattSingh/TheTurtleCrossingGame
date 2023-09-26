import time
from turtle import Screen

from car_manager import CarManager
from player import Player
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
game = Scoreboard()


screen.listen()
screen.onkey(player.move, "Up")

# Game loop
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    # Detect collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            game.game_over()

    # Update level
    if player.is_at_finish_line():
        game.update_level()
        player.reset_position()
        car_manager.increase_car_speed()

screen.exitonclick()
