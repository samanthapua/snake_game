from turtle import Turtle

starting_positions = [(0, 0), (-20, 0), (-40, 0)]
move_distance = 20

class Snake():
    def __init__(self):
        self.whole_snake = []
        self.create_snake()
        self.head = self.whole_snake[0]

    def create_snake(self):
        for position in starting_positions:
            self.add_segment(position)

    def add_segment(self,position):
            snake = Turtle("square")
            snake.color("white")
            snake.penup()
            snake.goto(position)
            self.whole_snake.append(snake)

    def extend(self):
        self.add_segment(self.whole_snake[-1].position())

    def move(self):
        for snake_segment in range(len(self.whole_snake)-1, 0,-1):
            new_x = self.whole_snake[snake_segment - 1].xcor()
            new_y = self.whole_snake[snake_segment -1].ycor()
            self.whole_snake[snake_segment].goto(new_x, new_y)
        self.head.forward(move_distance)

    def up(self):
        self.head.setheading(90)

    def down(self):
        self.head.setheading(270)

    def left(self):
        self.head.setheading(180)

    def right(self):
        self.head.setheading(0)