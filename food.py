import random
from turtle import Turtle
from random import Random

COLOR = ['purple','blue','lightblue','green','yellow','orange','pink']
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.fruits = []
        self.color('pink')
        self.shape('circle')
        self.shapesize(1,1)
        self.penup()
        self.set_ran_position()

    def set_ran_position(self):
        self.goto(random.randrange(-250,250), random.randrange(-250,250))

    def create_food(self, num_of_fruit):
        for i in range(num_of_fruit):
            fruit = Turtle()
            fruit.penup()
            fruit.hideturtle()
            fruit.color(random.choice(COLOR))
            fruit.shape('circle')
            fruit.goto(random.randrange(-250,250), random.randrange(-250,250))
            # fruit.set_ran_position()
            self.fruits.append(fruit)


    # def check_eat_food(self):




