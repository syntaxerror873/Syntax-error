import turtle

# Set up the screen
screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("skyblue")
screen.title("Simplified Lord Ram Drawing")

# Set up the turtle
t = turtle.Turtle()
t.speed(5)
t.width(3)
t.color("saddlebrown")

def draw_head():
    t.penup()
    t.goto(-50, 100)
    t.pendown()
    t.color("peachpuff")
    t.begin_fill()
    t.circle(30)  # Head
    t.end_fill()

def draw_body():
    t.penup()
    t.goto(-50, 70)
    t.pendown()
    t.color("blue")
    t.begin_fill()
    t.setheading(-90)
    t.forward(60)  # Body
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(60)
    t.end_fill()

def draw_arm():
    t.penup()
    t.goto(-50, 40)
    t.setheading(0)
    t.pendown()
    t.color("peachpuff")
    t.forward(50)  # Arm

def draw_bow():
    t.penup()
    t.goto(0, 40)
    t.setheading(90)
    t.pendown()
    t.color("darkgoldenrod")
    t.circle(50, 180)  # Bow

def draw_arrow():
    t.penup()
    t.goto(0, 90)
    t.pendown()
    t.setheading(0)
    t.color("gray")
    t.forward(80)  # Arrow shaft
    t.right(150)
    t.forward(15)  # Arrow tip
    t.backward(15)
    t.left(300)
    t.forward(15)  # Arrow tip
    t.hideturtle()

# Draw the figure
draw_head()
draw_body()
draw_arm()
draw_bow()
draw_arrow()

# Keep the window open until closed by the user
turtle.done()
