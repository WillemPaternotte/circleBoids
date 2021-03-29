import math
import random
import turtle

circleSize = 100
class point:
    def __init__(self, **kwargs):
        self.index = kwargs["index"] or 0
        self.x = random.randint(-50, 50)
        self.y = random.randint(-50, 50)
        self.rotation = random.randint(0, 360)
        self.point = turtle.Turtle()
        self.point.penup()
        self.point.speed(0)
        self.point.goto(self.x, self.y)
        self.point.pendown()
        self.point.setheading(self.rotation)

    def drawSqaure(self, size):
        for x in range(4):
            self.point.forward(size)
            self.point.right(90)
    
    def movement(self, oldPos, pos, circleSize):
        self.oldPos = oldPos
        self.pos = pos
        if self.pos[0] ** 2+self.pos[1] ** 2 >= circleSize**2:
            self.adx = 0 + self.pos[0]
            self.ady = 0 + self.pos[1]

            self.dx = self.oldPos[0]-self.pos[0]
            self.dy = self.oldPos[1]-self.pos[1]
            if self.dx != 0:
                self.rotation = math.degrees(math.atan(self.dy/self.dx))
            else:
                return 0

            if self.dx<0:
                if self.dy>0:
                    self.rotation += 360
            elif self.dx>0:
                self.rotation += 180
                
            self.m1 = self.ady / self.adx
            self.m2 = self.dy / self.dx
            if  self.m1*self.m2 != -1:
                self.inpactAngle = math.degrees(math.atan((self.m2 - self.m1)/(1+self.m1*self.m2)))
            else:
                return 0

            self.rotation += 180
            self.rotation -= 2*self.inpactAngle

            self.point.setheading(self.rotation)
            self.point.forward(2.5)

        else:
            self.point.forward(1)

circle = turtle.Turtle()
circle.hideturtle()
circle.speed(0)
circle.penup()
circle.goto(0,-(circleSize))
circle.pendown()
circle.circle(circleSize)

flock = []
for x in range(10):
    flock.append(point(index = x))

possitions = []
for point in flock:
    possitions.append(point.point.pos())
    point.point.forward(1)

time = 0  
while time < 200:
    oldPossitions = possitions
    for point in flock:
        possitions[point.index] = point.point.pos()

    for point in flock:
        point.movement(oldPossitions[point.index], possitions[point.index], circleSize)
    
    time +=1



turtle.mainloop()