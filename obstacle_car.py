from turtle import Turtle
from time import sleep
import random


class Car:
    """Creates the 'Car' class for the moving cars."""

    def __init__(self):
        """Initializes the attributes of the car."""
        self.all_cars = []
        self.x_distance = 5

    def create_car(self):
        """Creates a new car."""
        def random_color():
            """Makes the car a random color."""
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            rgb = (r, g, b)
            new_car.color(rgb)

        # makes sure a car is not created every time the create_car function
        # is called
        chance_of_making_car = random.randint(1, 7)
        if chance_of_making_car == 1:
            new_car = Turtle()
            new_car.shape('square')
            new_car.shapesize(stretch_len=2)
            new_car.penup()
            random_color()
            y_coordinate = random.randrange(-200, 200, 20)
            new_car.goto(320, y_coordinate)
            self.all_cars.append(new_car)

    def move_car(self):
        """Moves all the cars or removes it once it gets to the other side
        of the screen."""
        for car in self.all_cars:
            if car.xcor() > -350:
                x_coordinate = car.xcor() - self.x_distance
                car.goto(x_coordinate, car.ycor())
            else:
                self.all_cars.remove(car)

    def detect_collision(self, game_turtle):
        """Detects if there is a collision b/w the turtle and the cars."""
        for car in self.all_cars:
            if game_turtle.distance(car) < 20 and abs(car.xcor()) - 0 < 20:
                game_turtle.hideturtle()
                for car in self.all_cars:
                    car.hideturtle()
                return False

        return True
