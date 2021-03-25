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
pos = point.pos()
while time < 2000:
    oldPos = pos
    pos = point.pos()
    if math.pow(pos[0],2)+math.pow(pos[1],2) >= math.pow(circleSize,2):
        adx = 0 + pos[0]
        ady = 0 + pos[1]
        plane = ((math.atan(ady/adx)*180)/math.pi)

        dx = oldPos[0]-pos[0]
        dy = oldPos[1]-pos[1]

        cSquare = math.pow(dx, 2) + math.pow(dy, 2)
        rotation = math.degrees(math.asin(dy/math.sqrt(cSquare)))
        print(rotation)

        rotation = plane + (plane - rotation) + 90
        print(rotation)
        point.setheading(rotation)
        point.forward(1)
    else:
        point.forward(2.5)

    time += 1


turtle.mainloop()