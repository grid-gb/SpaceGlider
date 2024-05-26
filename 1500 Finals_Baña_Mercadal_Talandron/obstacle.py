import random
import turtle

obstacle_pics = ["obstacle_1.gif", "obstacle_3.gif"]  
random_color = ["pink", "light blue", "red"]

class Obstacle():
    def __init__(self):
        turtle.register_shape("green_bg.gif")
        turtle.register_shape("obstacle_1.gif")
        turtle.register_shape("obstacle_2.gif")
        turtle.register_shape("obstacle_3.gif")
        turtle.register_shape("starrrrr.gif")
        self.obstacle_list = []
        self.shape = random.choice(obstacle_pics)

    def create_obstacle(self):
        for _ in range(7):
            global obstacle
            obstacle = turtle.Turtle()
            obstacle.speed(0)  # pede ta machange as 0 or 10
            obstacle.hideturtle()

            shape = random.choice(obstacle_pics)
            shape = random.choice(obstacle_pics)
            color = random.choice(random_color)
            x = random.randint(-900, 900)
            obstacle.shape(shape)
            obstacle.color(color)
            obstacle.penup()
            obstacle.goto(x, 600)
            obstacle.fall_speed = random.randint(10, 20)  # Random fall speed para iba iba

            obstacle.showturtle()
            self.obstacle_list.append(obstacle)

        for _ in range(7):
            global resources
            resources = turtle.Turtle()
            resources.speed(0)  
            resources.hideturtle()
            x = random.randint(-900, 900)

            resources.shape("starrrrr.gif")
            resources.color(color)
            resources.penup()
            resources.goto(x, 600)
            resources.fall_speed = random.randint(10, 20)

            resources.showturtle()
            self.obstacle_list.append(resources)
