from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Courier', 14, 'bold')


class LevelDisplay(Turtle):
    """Class for object that displays the level."""

    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.color('white')
        self.penup()
        self.goto(-250, 260)
        self.display_level()

    def display_level(self):
        display_text = f"Level: {self.level}"
        self.write(arg=display_text, align=ALIGNMENT, font=FONT)

    def increase_level(self):
        self.level += 1
        self.display_level()

    def game_over_display(self):
        self.clear()
        self.home()
        game_over_msg = f"Game over! You got to level {self.level}."
        self.write(arg=game_over_msg, align=ALIGNMENT, font=FONT)
