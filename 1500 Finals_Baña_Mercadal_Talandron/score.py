import turtle

display_writer = turtle.Turtle()

class Score:
    def __init__(self):
        self.score = 0
        self.life = 3

    def update_display(self):
        display_writer.hideturtle()
        display_writer.penup()
        display_writer.goto(-900, 470)
        display_writer.color("white")
        display_writer.clear()
        display_writer.write(f"Score: {self.score}", align="left", font=("Fixedsys", 24, "normal"))
        display_writer.goto(-900, 430)
        display_writer.color("white")
        display_writer.write(f"Life: {self.life}", align="left", font=("Fixedsys", 24, "normal"))
    
    def clear(self):
        display_writer.clear()

