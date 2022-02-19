from turtle import Turtle


class MovingTurtle(Turtle):
    """Creates the moving turtle."""

    def __init__(self):
        """Initializes the attributes of the turtle."""
        super().__init__()
        self.shape('turtle')
        self.color('green')
        self.penup()
        self.go_to_starting_position()

    def go_to_starting_position(self):
        """Takes the turtle back to the starting position."""
        self.goto(0, -270)
        self.setheading(90)

    def move_up(self):
        """Makes the turtle go forward."""
        self.fd(15)

    def move_down(self):
        """Makes the turtle go backward."""
        self.backward(15)
