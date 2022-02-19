from time import sleep
from turtle import Turtle, Screen
from moving_turtle import MovingTurtle
from obstacle_car import Car
from level_display import LevelDisplay


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.colormode(255)
screen.tracer(0)

game_turtle = MovingTurtle()
car = Car()
level_display = LevelDisplay()

screen.listen()
screen.onkeypress(key="Up", fun=game_turtle.move_up)
screen.onkeypress(key="Down", fun=game_turtle.move_down)


game_active = True
car_speed = 0.05
while game_active:
    screen.update()
    sleep(car_speed)

    # checks if the turtle reached the other side
    if game_turtle.ycor() > 280:
        game_turtle.go_to_starting_position()
        car_speed *= 0.9
        level_display.increase_level()

    # creates and moves the car
    car.create_car()
    car.move_car()

    # detects collision b/w the turtle and the moving cars
    game_active = car.detect_collision(game_turtle)

screen.update()
level_display.game_over_display()

screen.exitonclick()
