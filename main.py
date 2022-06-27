from turtle import Screen
import time
from score_board import ScoreBoard
from snake import Snake
from food import Food

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


score_board = ScoreBoard()

game_is_on = True
score = 0
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    # detect collision with the food

    if(snake.head.distance(food) < 15):
        food.refresh()
        snake.extend()
        score_board.increase_score()

    # Detect collision with the wall

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score_board.reset()
        snake.reset()

    # Detect collision with it's own tail

    # for segment in snake.snake:
    #     if segment == snake.head:
    #         pass
    #     elif snake.head.distance(segment) < 10:
    #         game_is_on = False
    #         score_board.game_over()

    # Slicing:

    for segment in snake.snake[1:]:
        if snake.head.distance(segment) < 10:
            score_board.reset()
            snake.reset()


screen.exitonclick()
