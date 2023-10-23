from turtle import Turtle

init_position = [(0, 0), (20, 0), (40, 0)]


class Snake:
    def __init__(self):
        self.segment = []
        for p in init_position:
            new_s = self.crate_turtle(p)
            self.segment.append(new_s)
        self.head = self.segment[-1]

    def crate_turtle(self, position):
        new_snake = Turtle()
        new_snake.penup()
        new_snake.color('lime')
        new_snake.goto(position)
        new_snake.shape('square')
        return new_snake

    def go_up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def go_down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def go_left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def go_right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def move(self):
        # self.head.forward(10)
        for i in range(len(self.segment)-1):
            cur = self.segment[i]
            next = self.segment[i+1]
            cur.goto(next.pos())
        self.head.forward(10)

    def append_snake(self):
        s = self.segment[0]
        append_snake = self.crate_turtle(s.pos())
        self.segment.insert(0, append_snake)
