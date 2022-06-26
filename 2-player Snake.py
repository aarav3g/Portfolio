import turtle
import time
import random
colors = ["#1b700c", "#0c5e70", "#2d0c70", "#700c55", "#700c0c", "#70640c", "#4b700c", "#1ac4c2", "#c41ab6", "#b9c41a"]
shapes = ["square", "circle"]

delay = 0.1

score = 0
high_score = 0

wn = turtle.Screen()
wn.title("Snake")
wn.bgcolor("light grey")
wn.setup(width = 600, height = 600)
wn.tracer(0)

head = turtle.Turtle()
head.speed(0)
head.shape("circle")
head.color(random.choice(colors))
head.penup()
head.goto(0,0)
head.direction = "stop"

food = turtle.Turtle()
food.speed(0)
food.shape("square")
food.color("red")
food.penup()
food.goto(0,100)

segments = []

sc = turtle.Turtle()
sc.speed(0)
sc.shape(random.choice(shapes))
sc.color("black")
sc.penup()
sc.hideturtle()
sc.goto(0,260)
sc.write("Score: 0 | High score: 0", align = "center", font = ("Times New Roman", 24, "normal"))

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
        head.sety(y+20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y-20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x-20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x+20)

        
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")



while True:
    wn.update()

    if head.xcor() > 290 or head.xcor() < -290 or head.ycor()  > 290 or head.ycor() < - 290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"
    

        for segment in segments:
            segment.goto(1000,1000)
        segments.clear()
        score = 0
        delay = 0.1
        sc.clear()
        sc.write("Score: {} | High Score: {}".format(score, high_score), align = "center", font = ("Times New Roman", 24, "normal"))

    if head.distance(food) < 20:
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x,y)
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape(random.choice(shapes))
        new_segment.color(random.choice(colors))
        new_segment.penup()
        segments.append(new_segment)
    
        delay -= 0.001
        score+= 10

        if score > high_score:
            high_score = score
        sc.clear()
        sc.write("Score: {} | High Score: {}".format(score, high_score), align = "center", font = ("Times New Roman", 24, "normal"))

    for i in range(len(segments)-1,0,-1):
        x = segments[i -1].xcor()
        y = segments[i-1].ycor()
        segments[i].goto(x,y)
    if len(segments)>0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)

    move()

    for segment in segments:
        if segment.distance(head)<20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"

            for segment in segments:
                segment.goto(1000,1000)
            segments.clear()
            score = 0
            delay = 0.1

            sc.clear()
            sc.write("Score: {} | High Score: {}".format(score, high_score), align= "center", font = ("Times New Roman", 24, "normal"))
    time.sleep(delay)
wn.mainloop()
        
