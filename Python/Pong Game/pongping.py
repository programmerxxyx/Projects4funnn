from asyncio import Handle
import turtle

wn = turtle.Screen()
wn.title("Ping Pong Game by Esra")
wn.bgcolor("black")
wn.setup(width=1000, height=800)
wn.tracer(0)


#PA 
PA_a = turtle.Turtle()
PA_a.speed(0) 
PA_a.shape("square")
PA_a.shapesize(stretch_wid=6, stretch_len=1)
PA_a.color("white")
PA_a.penup()
PA_a.goto(-410, 0)

#PB 
PA_b = turtle.Turtle()
PA_b.speed(0) 
PA_b.shape("square")
PA_b.shapesize(stretch_wid=6, stretch_len=1)
PA_b.color("white")
PA_b.penup()
PA_b.goto(400, 0)

#Ball
ball = turtle.Turtle()
ball.speed(0) 
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx =  0.1
ball.dy = -0.1


# Pen

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 350)
pen.write("Player A: 0    Player B: 0", align="center", font=("Courier", 24, "normal"))

#function aaaa
def PA_a_up():
    y = PA_a.ycor()
    y += 20 
    PA_a.sety(y)


#function AAAAA
def PA_a_down():
    y = PA_a.ycor()
    y -= 20 
    PA_a.sety(y)


#function bbbbb
def PA_b_up():
    y = PA_b.ycor()
    y += 20 
    PA_b.sety(y)


#function BBBB
def PA_b_down():
    y = PA_b.ycor()
    y -= 20 
    PA_b.sety(y)



#keyboard 
wn.listen() 
wn.onkeypress(PA_a_up, "w")
wn.onkeypress(PA_a_down, "s")

wn.onkeypress(PA_b_up, "Up")
wn.onkeypress(PA_b_down, "Down")


# main game loop 

while True: 
    wn.update()

    #movin le balls 
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #Border 
    if ball.ycor() > 400:
        ball.sety(400)
        ball.dy *= -1

    #Border 
    if ball.ycor() < -400:
        ball.sety(-400)
        ball.dy *= -1

    if ball.xcor() > 500:
        ball.goto(0, 0)
        ball.dx *= -1


    if ball.xcor() < -500:
        ball.goto(0, 0)
        ball.dx *= -1


    
    # Paddle and ball colliding :)

  
    if ball.xcor()> 380 and (ball.ycor() < PA_b.ycor() + 40 and ball.ycor() > PA_b.ycor() -40):    
        ball.setx(380)
        ball.dx *= -1


    if ball.xcor() < -380 and (ball.ycor() > PA_a.ycor() + 40 and ball.ycor() > PA_a.ycor() -40):
        ball.setx(-380)
        ball.dx *= -1