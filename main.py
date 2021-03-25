import turtle
import random
import math

window = turtle.Screen()
window.bgcolor("black")
window.title("simulatie")

circleSize = 200

circle = turtle.Turtle()
circle.color("white")
circle.hideturtle()
circle.speed(0)
circle.penup()
circle.goto(0,-(circleSize))
circle.pendown()
circle.circle(circleSize)


x = random.randint(-50, 50)
y = random.randint(-50, 50)
rotation = random.randint(0, 360)
point = turtle.Turtle()
point.color("white")
point.penup()
point.speed(0)
point.goto(x, y)
point.setheading(rotation)


time = 0
while time < 500:
    pos = point.pos()
    if not(math.pow(pos[0],2)+math.pow(pos[1],2) >= math.pow(circleSize,2)):
        point.forward(5)
    else:
        dx = 0 + pos[0]
        dy = 0 + pos[1]
        plane = ((math.atan(dy/dx)*180)/math.pi)
        print(plane)

        rotation = plane + (plane - rotation) -180
        point.setheading(rotation)
        point.forward(2.5)
        
    
    oldPos = pos
    time += 1


turtle.mainloop()