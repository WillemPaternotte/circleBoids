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


A = turtle.Turtle()
B = turtle.Turtle()
C = turtle.Turtle()
D = turtle.Turtle()
E = turtle.Turtle()

points = [A,B,C,D,E]

for point in points:
    x = random.randint(-50, 50)
    y = random.randint(-50, 50)
    rotation = random.randint(0, 360)
    point.color("white")
    point.penup()
    point.speed(0)
    point.goto(x, y)
    point.setheading(rotation)
    point.pendown()

def movement(object, oldPos, pos, circleSize):
    if pos[0] ** 2+pos[1] ** 2 >= circleSize**2:
        adx = 0 + pos[0]
        ady = 0 + pos[1]

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

        object.setheading(rotation)
        object.forward(2.5)

    else:
        object.forward(1)

def steering(object, oldPos, pos, points):
    distance = 10000
    for point in points:
        if point != object:
            # if object.distance(point)< distance:
            #     distance = object.distance(point)
            #     nearestPoint = point

            if object.distance(point) < 25: 
                adx = abs(point.pos()[0] - pos[0])
                ady = abs(point.pos()[1] - pos[1])


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
        
                if 0<inpactAngle<90:
                    object.left(5)
                elif -90<inpactAngle<0:
                    object.right(5) 
    
time = 0

Apos = A.pos()
Bpos = B.pos()
Cpos = C.pos()
Epos = E.pos()
Dpos = D.pos()

A.forward(1)
B.forward(1)
C.forward(1)
D.forward(1)
E.forward(1)

while time < 2000:
    AoldPos = Apos
    Apos = A.pos()
    movement(A, AoldPos, Apos, circleSize)
    steering(A, AoldPos, Apos, points)

    BoldPos = Bpos
    Bpos = B.pos()
    movement(B, BoldPos, Bpos, circleSize)
    steering(B, BoldPos, Bpos, points)

    ColdPos = Cpos
    Cpos = C.pos()
    movement(C, ColdPos, Cpos, circleSize)
    steering(C, ColdPos, Cpos, points)

    DoldPos = Dpos
    Dpos = D.pos()
    movement(D, DoldPos, Dpos, circleSize)
    steering(D, DoldPos, Dpos, points)

    EoldPos = Epos
    Epos = E.pos()
    movement(E, EoldPos, Epos, circleSize)
    steering(E, EoldPos, Epos, points)

    




       

    time += 1


turtle.mainloop()