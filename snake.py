from pickle import STACK_GLOBAL
from turtle import Turtle, right

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake():
    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]

    # Creating 3 new segments and putting them in an order
    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

            # moving the snake, making the segments follow each other while only the first segment moves forward

    def move(self):
        for n in range(len(self.snake)-1, 0, -1):
            new_X = self.snake[n-1].xcor()
            new_Y = self.snake[n-1].ycor()
            self.snake[n].goto(new_X, new_Y)
        self.snake[0].forward(MOVE_DISTANCE)

    def add_segment(self, position):
        newSegments = Turtle("square")
        newSegments.penup()
        newSegments.color("white")
        newSegments.goto(position)
        self.snake.append(newSegments)

    def extend(self):
        self.add_segment(self.snake[-1].position())

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def reset(self):
        for seg in self.snake:
            seg.goto(1000, 1000)
        self.snake.clear()
        self.create_snake()
        self.head = self.snake[0]
