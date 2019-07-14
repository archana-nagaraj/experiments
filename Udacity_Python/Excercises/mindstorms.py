import turtle
def draw_square(some_turtle):
    noOfLines = 4
    count = 1
    while count <= noOfLines:
        some_turtle.forward(200)
        some_turtle.right(90)
        count = count + 1 

def draw_circle():
    groove = turtle.Turtle()
    groove.color("blue")
    groove.circle(100)
    groove.shape("arrow")

def draw_triangle():
    tray = turtle.Turtle()
    tray.color("green")
    noOfLines = 3
    count = 1
    while count <= noOfLines:
        tray.forward(100)
        tray.left(120)
        tray.forward(100)
        count = count + 1
def draw_shape():
    myScreen = turtle.Screen()
    myScreen.bgcolor("green")
    #draw_circle()
    #draw_triangle()
    brad = turtle.Turtle()
    for i in range(1,37):
        draw_square(brad)
        brad.right(10)
    myScreen.exitonclick()
draw_shape()