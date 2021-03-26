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
    if pos[0] ** 2+pos[1] ** 2 >= circleSize**2:
        adx = 0 + pos[0]
        ady = 0 + pos[1]
        plane = ((math.atan(ady/adx)*180)/math.pi)

        dx = oldPos[0]-pos[0]
        dy = oldPos[1]-pos[1]
        rotation = math.degrees(math.atan(dy/dx))

        if dx<0:
            if dy>0:
                rotation += 360
        elif dx>0:
            rotation += 180
            
        m1 = ady / adx
        m2 = dy / dx
        inpactAngle = math.degrees(math.atan((m2 - m1)/(1+m1*m2)))

        rotation += 180
        rotation -= 2*inpactAngle

        point.setheading(rotation)
        point.forward(2.5)
       
    else:
        point.forward(1)

    time += 1


turtle.mainloop()