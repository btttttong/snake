import time
from score import Score
from food import Food
from snake1 import Snake
from turtle import Screen

screen = Screen()
screen.setup(800, 600)
food = Food()
snake = Snake()
score = Score()
screen.listen()
is_game_on = True
snake_speed = 0.1
screen.tracer(0)
num_of_fruit = 1

screen.onkeypress(fun=snake.go_up, key="Up")
screen.onkeypress(fun=snake.go_down, key="Down")
screen.onkeypress(fun=snake.go_right, key="Right")
screen.onkeypress(fun=snake.go_left, key="Left")



while is_game_on:
    # screen.write()
    time.sleep(snake_speed)
    screen.update()
    score.print_current_score()
    score.print_high_score()
    snake.move()
    if snake.head.distance(food) < 10:
        food.create_food(num_of_fruit)
        # food.set_ran_position()
        num_of_fruit += 1
        print(num_of_fruit)
        score.add_score()

        print(len(food.fruits))
        snake.append_snake()
        score.print_current_score()
        if snake_speed >= 0.1:
            snake_speed -= 0.001


    # detect wall
    if snake.head.ycor() < -300 or snake.head.ycor() > 300 or snake.head.xcor() < -300 or snake.head.xcor() > 300:
        score.print_over()
        is_game_on = False


# stay on screen
screen.mainloop()
