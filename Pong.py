import turtle
wind = turtle.Screen()
wind.title("Pong")
wind.bgcolor("grey")
wind.setup(width = 800, height = 600)
wind.tracer(0.5)

bar_A = turtle.Turtle()
bar_A.shape("square")
bar_A.color("black")
bar_A.shapesize(stretch_wid = 7, stretch_len = 1)
bar_A.penup()
bar_A.goto(-350, 0)

bar_B = turtle.Turtle()
bar_B.shape("square")
bar_B.color("black")
bar_B.shapesize(stretch_wid = 7, stretch_len = 1)
bar_B.penup()
bar_B.goto(350, 0)


ball = turtle.Turtle()
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball_x = 0.3
ball_y = 0.2

sboard = turtle.Turtle()
sboard.shape("square")
sboard.color("white")
sboard.penup()
sboard.hideturtle()
sboard.goto(0,260)
sboard.write("Player A: 0 | Player B: 0", align = "center", font = ("Times New Roman", 24, "normal"))

score_a = 0
score_b = 0

def bar_A_up():
    y = bar_A.ycor()
    y+= 30
    bar_A.sety(y)

def bar_A_down():
    y = bar_A.ycor()
    y-= 30
    bar_A.sety(y)

def bar_B_up():
    y = bar_B.ycor()
    y+= 30
    bar_B.sety(y)

def bar_B_down():
    y = bar_B.ycor()
    y-= 30
    bar_B.sety(y)



wind.listen()
wind.onkeypress(bar_A_up, "w")
wind.onkeypress(bar_A_down, "s")
wind.onkeypress(bar_B_up, "Up")
wind.onkeypress(bar_B_down, "Down")

while True:
    wind.update()

    ball.setx(ball.xcor() + ball_x)
    ball.sety(ball.ycor() + ball_y)

    if ball.ycor() > 290:
        ball.sety(290)
        ball_y *= - 1
    elif ball.ycor() < -290:
        ball.sety(-290)
        ball_y *= -1


    if ball.xcor() > 350:
        score_a += 1
        sboard.clear()
        sboard.write("Player A: {} | Player B: {}".format(score_a, score_b), align = "center", font = ("Times New Roman", 24, "normal"))
        ball.goto(0,0)
        ball_x *= -1
    elif ball.xcor() <-350:
        score_b += 1
        sboard.clear()
        sboard.write("Player A: {} | Player B: {}".format(score_a, score_b), align = "center", font = ("Times New Roman", 24, "normal"))
        ball.goto(0,0)
        ball_x *= -1

    if ball.xcor() <-340 and ball.ycor() + 50 and ball.ycor() > bar_A.ycor() - 50:
        ball_x *= -1
    elif ball.xcor() > 340 and ball.ycor() + 50 and ball.ycor() > bar_B.ycor() - 50:
        ball_x *= -1
