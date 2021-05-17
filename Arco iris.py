import turtle

fas = turtle.Turtle()
fas.speed(0)
fas.goto(0, 0)
fas.pensize(3)

def square(length, angle):
    for i in range(4):
      fas.forward(length)
      fas.left(angle)

for i in range(13):
    for colors in ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]:
        fas.color(colors)
        square(200, 90)
        fas.left(91)
    
