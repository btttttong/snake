from turtle import Turtle
# import highscore
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 50
        try:
            f = open("highscore.txt", "r")
            self.highscore = int(f.read())
            f.close()
        except ValueError:
            self.highscore = 0


    def add_score(self):
        self.score += 1
        print(f'your score = {self.score}')
        return self.score

    def print_current_score(self):
        self.clear()
        self.penup()
        self.hideturtle()
        self.goto(-200, 250)
        self.write(f'Your Score: {self.score}', align='center', font=('Tahoma', 20, 'normal'))

    def print_high_score(self):
        self.penup()
        self.hideturtle()
        self.goto(150, 250)
        if self.score >= self.highscore:
            self.write(f'High Score: {self.score}', align='center', font=('Tahoma', 20, 'normal'))
            with open("highscore.txt", "w") as f:
                f.write(str(self.score))
        else:
            self.write(f'High Score: {self.highscore}', align='center', font=('Tahoma', 20, 'normal'))