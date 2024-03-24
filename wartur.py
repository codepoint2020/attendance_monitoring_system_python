from turtle import Turtle, Screen

genbu = Turtle()
screen = Screen()

genbu.shape("circle")
genbu.color("green")


def make_square():
    genbu.pendown()
    genbu.pencolor("#FF3EA5")
    for _ in range(4):
        genbu.forward(200)
        genbu.left(90)


def make_triangle():
    genbu.pendown()
    genbu.pencolor("#9400FF")
    for _ in range(3):

        genbu.forward(150)
        genbu.left(120)


def make_hex():
    genbu.pendown()
    genbu.pencolor("#7F27FF")
    for _ in range(6):
        genbu.forward(100)
        genbu.left(60)


def ultimate_skill():
    genbu.pendown()
    genbu.pencolor("red")
    make_hex()

    
    move_jump()  
    genbu.pendown()
    genbu.pencolor("cyan")
    make_square()
    
    move_jump()
    genbu.pendown()
    genbu.pencolor("violet")
    make_triangle()

    
    genbu.right(360)

def move_jump():
    genbu.penup()
    genbu.forward(50)
   


def move_forward():
    genbu.penup()
    genbu.forward(10)


def move_backward():
    genbu.penup()
    genbu.backward(10)


def move_left():
    genbu.penup()
    genbu.left(10)


def move_right():
    genbu.penup()
    genbu.right(10)



screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="a", fun=move_left)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="d", fun=move_right)
screen.onkey(key="space", fun=move_jump)

#Skills
screen.onkey(key="q", fun=make_square)
screen.onkey(key="t", fun=make_triangle)
screen.onkey(key="h", fun=make_hex)
screen.onkey(key="u", fun=ultimate_skill)




screen.exitonclick()