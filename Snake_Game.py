import turtle
import random
import time

# Default Values
delay = 0.08
score = 0
high_score = 0

# Creating the screen
screen = turtle.Screen()
screen.title('Snake Game')
screen.bgcolor('black')
screen.setup(1000, 1000)
screen.tracer(0)

# Creating the head of the snake
head = turtle.Turtle()
head.shape('square')
head.color('white')
head.penup()
head.goto(0, 0)
head.direction = 'Stop'

# Creating the food
food = turtle.Turtle()
food.speed(0)
food.color('blue')
food.shape('circle')
food.shapesize(0.95, 0.95, 1)
food.penup()
food.goto(0, 100)

# Creating text
text = turtle.Turtle()
text.speed(0)
text.color('yellow')
text.penup()
text.hideturtle()
text.goto(0, 450)
text.write('Score: 0 High Score: 0', align='center',
           font=('calibri', 28, 'bold'))


# Movement commands
def up():

    if head.direction != 'down':
        head.direction = 'up'


def down():

    if head.direction != 'up':
        head.direction = 'down'


def left():

    if head.direction != 'right':
        head.direction = 'left'


def right():

    if head.direction != 'left':
        head.direction = 'right'


def movement():

    if head.direction == 'up':
        y = head.ycor()
        head.sety(y+20)

    if head.direction == 'down':
        y = head.ycor()
        head.sety(y-20)

    if head.direction == 'left':
        x = head.xcor()
        head.setx(x-20)

    if head.direction == 'right':
        x = head.xcor()
        head.setx(x+20)


# Movement inputs
screen.listen()
screen.onkeypress(up,  'w')
screen.onkeypress(down,  's')
screen.onkeypress(left,  'a')
screen.onkeypress(right,  'd')

# Setting tail to 0
segments = []

# Game Logic
while True:

    screen.update()

    # Check for out of bounds and reset game
    if head.xcor() > 490 or head.xcor() < -490 or head.ycor() > 490 or head.ycor() < -490:

        time.sleep(1)
        head.goto(0, 0)
        head.direction = 'Stop'

        for segment in segments:

            segment.goto(1500, 1500)

        segments.clear()
        score = 0
        delay = 0.1
        text.clear()
        text.write(f'Score: {score} High Score: {high_score} ', align='center',
                   font=('calibri', 28, 'bold'))

    # Place food
    if head.distance(food) < 20:

        x = random.randint(-470, 470)
        y = random.randint(-470, 470)
        food.goto(x, y)

        # Add new segment if head reaches food
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape('square')
        new_segment.color('white')
        new_segment.penup()
        segments.append(new_segment)

        # Score and speed update
        delay -= 0.001
        score += 10

        if score > high_score:

            high_score = score

        text.clear()
        text.write(f'Score: {score} High Score: {high_score} ', align='center',
                   font=('calibri', 28, 'bold'))

    # Check for collision and reset game
    for i in range(len(segments)-1, 0, -1):

        x = segments[i-1].xcor()
        y = segments[i-1].ycor()
        segments[i].goto(x, y)

    if len(segments) > 0:

        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    movement()

    for segment in segments:

        if segment.distance(head) < 15:

            time.sleep(1)
            head.goto(0, 0)
            head.direction = 'Stop'

            for segment in segments:

                segment.goto(1500, 1500)

            segments.clear()
            score = 0
            delay = 0.1
            text.clear()
            text.write(f'Score: {score} High Score: {high_score} ',
                       align='center', font=('calibri', 28, 'bold'))

    time.sleep(delay)

screen.mainloop()
