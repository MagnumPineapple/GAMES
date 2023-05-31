import turtle
import time
import random

delay = 0.1

# Score
score = 0
high_score = 0

# Set up the screen
wn = turtle.Screen()
wn.title("SNAKE")
wn.bgcolor("dark green")
wn.setup(width=1280, height=720)
wn.tracer(0)  # Turns off the screen updates

# Snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Snake food
food = turtle.Turtle()
food.speed(0)
food.shape("square")
food.color("red")
food.penup()
food.goto(0, 100)

segments = []

# Borders
borders = turtle.Turtle()
borders.speed(0)
borders.color("white")
borders.penup()
borders.goto(-300, -300)
borders.pendown()
borders.pensize(4)
for _ in range(4):
    borders.forward(600)
    borders.left(90)
borders.hideturtle()

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Puntuación: 0  | TOP Puntuación: 0", align="center", font=("Courier", 16, "normal"))

# Timer
timer_pen = turtle.Turtle()
timer_pen.speed(0)
timer_pen.shape("square")
timer_pen.color("white")
timer_pen.penup()
timer_pen.hideturtle()
timer_pen.goto(0, -300)
timer_start = time.time()

# Functions
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

def add_segment():
    new_segment = turtle.Turtle()
    new_segment.speed(0)
    new_segment.shape("square")
    new_segment.color("grey")
    new_segment.penup()
    segments.append(new_segment)

# Keyboard bindings
wn.listen()
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")

# Main game loop
while True:
    wn.update()

    # Check for a collision with the border
    if (
        head.xcor() > 290
        or head.xcor() < -290
        or head.ycor() > 290
        or head.ycor() < -290
    ):
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"

        # Hide the segments
        for segment in segments:
            segment.goto(1000, 1000)

        # Clear the segments list
        segments.clear()

        # Reset the score
        score = 0

        # Reset the delay
        delay = 0.1

        pen.clear()
        pen.write(
            "Puntuación: {}  TOP Puntuación: {}".format(score, high_score),
            align="center",
            font=("Courier", 16, "normal"),
        )

    # Check for a collision with the food
    if head.distance(food) < 20:
        # Move the food to a random spot
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        # Add a segment
        add_segment()

        # Shorten the delay
        delay -= 0.001

        # Increase the score
        score += 1

        if score > high_score:
            high_score = score

        pen.clear()
        pen.write(
            "Puntuación: {}  TOP Puntuación: {}".format(score, high_score),
            align="center",
            font=("Courier", 16, "normal"),
        )

    # Move the end segments first in reverse order
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    # Move segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()

    # Check for head collision with the body segments
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

            # Hide the segments
            for segment in segments:
                segment.goto(1000, 1000)

            # Clear the segments list
            segments.clear()

            # Reset the score
            score = 0

            # Reset the delay
            delay = 0.1

            pen.clear()
            pen.write(
                "Puntuación: {}  TOP Puntuación: {}".format(score, high_score),
                align="center",
                font=("Courier", 16, "normal"),
            )

    # Update timer
    elapsed_time = int(time.time() - timer_start)
    hours = elapsed_time // 3600
    minutes = (elapsed_time % 3600) // 60
    seconds = (elapsed_time % 3600) % 60
    timer_pen.clear()
    timer_pen.write(
        "Tiempo: {} horas, {} minutos, {} segundos".format(hours, minutes, seconds),
        align="center",
        font=("Courier", 12, "normal"),
    )

    time.sleep(delay)

wn.mainloop()
