import turtle
import random
from obstacle import Obstacle
from score import Score
import time

#A Game by:
#Elyon Francine A. Baña
#Kent Lloyd Mercadal
#Jann Gabriel Talandron


# Register shapes
turtle.register_shape("Moon_Phase_1.gif")
turtle.register_shape("green_bg.gif")
turtle.register_shape("sprite.gif")
turtle.register_shape("collision.gif")
turtle.register_shape("starrrrr.gif")
turtle.register_shape("obstacle_1.gif")
turtle.register_shape("obstacle_3.gif")

# SCREEN
screen = turtle.Screen()
screen.setup(width=1.0, height=1.0)
screen.title('SPACE GAME')
screen.bgpic("green_bg.gif")
screen.tracer(0)

# PEN
pen = turtle.Turtle()
pen.hideturtle()
pen.pencolor('#FFFFFF')
pen.fillcolor('white')
pen.shape("Moon_Phase_1.gif")
pen.penup()
pen.showturtle()
pen.goto(0, 0.350 * screen.window_height())

# LOCATIONS
pen_coordinates = [130, 50, 0, -50, -100]
pen_coordinates2 = [40, 0, -45, -100]
pen_message = ["SPACE GLIDER", "Main Menu", "Play", "Credits", "Exit"]

pen_size = [100, 24, 16, 16, 16, 16]
font_setting = ["bold", "normal", "normal", "normal", "normal"]

credits=["Elyon Francine A. Baña", "Kent Lloyd Mercadal", "Jann Gabriel Talandron", "-----Back to Main Menu-----"]


menu = turtle.Turtle()
home=turtle.Turtle()
home.hideturtle()
home.penup()
home.pencolor("white")

game_over=turtle.Turtle()
game_over=turtle.Turtle()
game_over.hideturtle()
game_over.penup()
game_over.pencolor("white")

get=turtle.Turtle()
dont_get1=turtle.Turtle()
dont_get2=turtle.Turtle()
instructions=turtle.Turtle()

# Draw stars
def draw_stars():
    star = turtle.Turtle()
    star.color('white')
    star.penup()
    star.hideturtle()
    for _ in range(100):
        x = random.randint(-1000, 1000)
        y = random.randint(-1000, 1000)
        star.goto(x, y)
        star.dot(3)


# Draw menu
def draw_menu(type):
    if type == "main":
        for message, size, font, coordinate in zip(pen_message, pen_size, font_setting, pen_coordinates):
            menu.hideturtle()
            menu.color("white")
            menu.penup()
            menu.goto(0, coordinate)
            menu.write(message, align="center", font=("Fixedsys", size, font))
        

    if type == "how to play":
        menu.goto(0,130)
        menu.write("SPACE GLIDER", align="center", font=("Fixedsys", 100, "bold"))
        menu.goto(0, 80)
        menu.write("Credits", align="center", font=("Fixedsys", 24, "bold"))

        for message2, coordinates2 in zip(credits, pen_coordinates2):
            menu.goto(0, coordinates2)
            menu.write(message2, align="center", font=("Fixedsys", 16, "normal"))
        




# Main menu
def main_Menu(x, y):
    startx, starty, startLength, startWidth = -40, 0, 65, 25
    optionsx, optionsy, optionsLength, optionsWidth = -40, -50, 75, 25
    endx, endy, endLength, endWidth = -60, -100, 130, 25

    if optionsx <= x <= optionsx + optionsLength and optionsy <= y <= optionsy + optionsWidth:
        print('Options Clicked')
        return "how to play"
    if startx <= x <= startx + startLength and starty <= y <= starty + startWidth:
        print('Clicked')
        return "start"
    if endx <= x <= endx + endLength and endy <= y <= endy + endWidth:
        print('Clicked')
        return "back"

signal = "no"

# Key bindings
def left():
    global signal
    signal = "left"

def right():
    global signal
    signal = "right"

def hide_collision(collision):
    collision.hideturtle()

def hide_star_collision(star_collision):
    star_collision.clear()


def return_object(obstacle):
    obstacle.hideturtle()
    x = random.randint(-900, 900)
    obstacle.goto(x, 540)
    obstacle.fall_speed = random.randint(10, 20)
    obstacle.showturtle()


def show_game_over():
    game_over.penup()
    game_over.goto(0, 0)
    game_over.write("GAME OVER", align="center", font=("Fixedsys", 100, "bold"))



def clear_game_objects(character, obstacles, collision, score):
    character.hideturtle()
    collision.hideturtle()
    for obstacle in obstacles:
        obstacle.hideturtle()
    score.clear()


#reused the main menu busttons
def handle_click_for_go_home(x,y):
    action = main_Menu(x, y)
    if action == "how to play":
        home.clear()
        game_over.clear()
        screen.bgcolor("black")
        screen.onclick(None)
        screen.update()
        HOME()
        print("Entering Options Menu...")
    elif action == "back":
        quit()

#game proper
def start_game():
    instructions.clear()
    get.hideturtle()
    dont_get1.hideturtle()
    dont_get2.hideturtle()

    global signal
    screen.bgpic("green_bg.gif")

    collision = turtle.Turtle()
    collision.hideturtle()
    collision.shape("collision.gif")
    collision.penup()

    star_collision = turtle.Turtle()
    star_collision.hideturtle()
    star_collision.pencolor("white")
    star_collision.penup()

    character = turtle.Turtle()
    character.penup()
    character.setposition(0, -350)
    character.shape("sprite.gif")
    signal = "no"

    obstacle = Obstacle()
    obstacle.create_obstacle()
    screen.listen()
    screen.onkeypress(left, "a")
    screen.onkeypress(right, "d")
    score = Score()
    is_on = True

    while is_on:
        screen.onclick(None)
        score.update_display()
        screen.update()
        time.sleep(0.1)

        if signal == "left":
            character.setx(character.xcor() - 40)
            signal = "no"
            if character.xcor() < -900:
                character.setx(-895)

        if signal == "right":
            character.setx(character.xcor() + 40)
            signal = "no"
            if character.xcor() > 900:
                character.setx(895)

        for obstacle_movement in obstacle.obstacle_list:
            obstacle_movement.sety(obstacle_movement.ycor() - obstacle_movement.fall_speed)
            if obstacle_movement.ycor() <= -450:
                return_object(obstacle_movement)
        
        for obstacle_movement in obstacle.obstacle_list:
            shape = obstacle_movement.shape()
            if check_collision(character, obstacle_movement, 35, 25): #setting the radius ka character and obstacle
                print("Collision!")
                if shape == "starrrrr.gif":
                    star_collision.goto(obstacle_movement.pos())
                    star_collision.pendown()
                    star_collision.write("+40 points", align="center", font=("Fixedsys", 16, "bold"))
                    star_collision.penup()
                    screen.ontimer(lambda: hide_star_collision(star_collision), 300)
                    return_object(obstacle_movement)
                    score.score += 40
                    print("Obtained points")
                        
                else:
                    collision.goto(obstacle_movement.pos())
                    collision.showturtle()
                    screen.ontimer(lambda: hide_collision(collision), 100)
                    if score.life > 0:
                        return_object(obstacle_movement)
                        screen.ontimer(lambda: hide_collision(collision), 300)
                        score.life -= 1
                        print("lose life")
                            
                    elif score.life == 0:
                        collision.showturtle()
                        collision.goto(obstacle_movement.pos())
                        
                        screen.update()
                        show_game_over()
                        go_home()
                        screen.update()
                        clear_game_objects(character, obstacle.obstacle_list, collision, score)
                        is_on = False

def check_collision(player, obstacle, player_radius, obstacle_radius):
    player_x, player_y = player.position()
    obstacle_x, obstacle_y = obstacle.xcor(), obstacle.ycor()

    distance = ((player_x - obstacle_x) ** 2 + (player_y - obstacle_y) ** 2) ** 0.5
    return distance <= player_radius + obstacle_radius


# Handle click for options
def handle_click_for_options(x, y):
    action = main_Menu(x, y)
    if action == "back":
        menu.clear()
        draw_menu("main")
        screen.onclick(handle_click_for_main)
    else:
        print("none")


def game_instructions():
        get.penup()
        get.hideturtle()
        get.goto(-200,390)
        get.shape("starrrrr.gif")
        get.showturtle()

        dont_get1.penup()
        dont_get1.hideturtle()
        dont_get1.goto(0,390)
        dont_get1.shape("obstacle_1.gif")
        dont_get1.showturtle()

        dont_get2.penup()
        dont_get2.hideturtle()
        dont_get2.goto(200,390)
        dont_get2.shape("obstacle_3.gif")
        dont_get2.showturtle()

        instructions.penup()
        instructions.hideturtle()
        instructions.goto(0,250)
        instructions.color("white")

        instructions.pendown()
        instructions.write("Catch the stars to earn points", align="center", font=("Fixedsys", 18, "normal"))
        instructions.penup()
        instructions.goto(0,150)

        instructions.pendown()
        instructions.write("Avoid the asteroids", align="center", font=("Fixedsys", 18, "normal"))
        instructions.penup()
        instructions.goto(0,50)

        instructions.pendown()
        instructions.write("You only have 3 lives", align="center", font=("Fixedsys", 18, "normal"))
        instructions.penup()
        instructions.goto(0,-50)

        instructions.pendown()
        instructions.write("Press 'a' to move left and Press 'd' to move right ", align="center", font=("Fixedsys", 18, "normal"))
        instructions.penup()
        instructions.goto(0,-150)

        instructions.pendown()
        instructions.write("You can catch the stars from above and the side", align="center", font=("Fixedsys", 18, "normal"))
        instructions.penup()
        instructions.goto(0,-250)

        instructions.pendown()
        instructions.write("You cannot gain points or get hurt if the stars and asteroids reach your feet", align="center", font=("Fixedsys", 18, "normal"))
        instructions.penup()
        instructions.goto(0,-350)

        instructions.pendown()
        instructions.write("-----CLICK ANYWHERE TO START-----", align="center", font=("Fixedsys", 20, "bold"))

        screen.onclick(lambda x, y: start_game())
        screen.update()




# Handle click for main
def handle_click_for_main(x, y):
    action = main_Menu(x, y)
    if action == "start":
        print("Starting...")
        menu.clear()
        pen.hideturtle()
        screen.update()
        game_instructions()
        screen.update()

    elif action == "how to play":
        menu.clear()
        draw_menu("how to play")
        screen.onclick(handle_click_for_options)
        print("Entering Options Menu...")
    elif action == "back":
        quit()


def go_home():
    home.goto(0,-50)
    home.write("Home", align="center", font=("Fixedsys", 20, "normal"))
    home.goto(0,-100)
    home.write("Exit", align="center", font=("Fixedsys", 20, "normal"))
    screen.onclick(handle_click_for_go_home)
    screen.update()


# Home screen
def HOME():
    screen.bgcolor("black")
    draw_stars()
    draw_menu("main")
    screen.onclick(handle_click_for_main)
    screen.update()

HOME()
turtle.done()

