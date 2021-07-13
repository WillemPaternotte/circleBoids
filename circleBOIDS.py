import math
import random
import turtle

#sets up the screen
window = turtle.Screen()
window.bgcolor("black")
window.title("circleBOIDS")

class point: #wow points class, so cool
    def __init__(self, **kwargs):
        self.index = kwargs["index"] or 0
        self.x = random.randint(-50, 50)
        self.y = random.randint(-50, 50)
        self.rotation = random.randint(0, 360)
        self.point = turtle.Turtle()
        self.point.penup()
        self.point.color("white")
        self.point.speed(0)
        self.point.goto(self.x, self.y)
        self.point.setheading(self.rotation)

    def movement(self, oldPos, pos, circleSize): #makes points move foward and stay inside the circle
        if pos[0] ** 2+ pos[1] ** 2 >= circleSize**2: # if outside circle turn around
            self.inpactAngle = twoPointAngle(oldPos, pos, [0,0])

            self.rotation = self.point.heading()   

            self.rotation += 180
            self.rotation -= 2*self.inpactAngle

            self.point.setheading(self.rotation)
            self.point.forward(3)

        else:
            self.point.forward(1)

    def steering(self, **kwargs): # all steering function combined in 1
        # self.index = kwargs["index"]
        possitions = kwargs["possitions"]
        oldPossitions = kwargs["oldPossitions"]
        flock = kwargs["flock"]

        oldLocalFlock = []
        localFlock = []
        for point in flock: 
            if point.index != self.index:
                if self.point.distance(point.point.pos())< 45: #gets only the local flock
                    oldLocalFlock.append(oldPossitions[point.index])
                    localFlock.append(possitions[point.index])
        
        turning = 0
        if len(localFlock)!= 0:
            centerOldLocalFlock = flockCenter(oldLocalFlock)
            centerLocalFlock = flockCenter(localFlock)
            localFlockHeading = rotation(centerOldLocalFlock, centerLocalFlock)
            heading =  self.point.heading()

            turning += self.centring(centerLocalFlock, heading) * 4 #tweak multipliers to change beheavour 
            turning += self.aligning(localFlockHeading, heading) * 4
            turning += self.avoiding(localFlock, heading) * 6
        self.point.right(turning)
        
    def avoiding(self, localFlock, heading): #complicated code that handles avoiding
        turning = 0
        for point in localFlock:
            angle = self.point.towards(point) - heading #twoPointAngle(oldPossitions[self.index], possitions[self.index], possitions[point.index])
            if angle > 180:
                angle -= 360
            elif angle < -180:
                        angle += 360
            if 0<=angle< 120:
                turning += 1
            elif -120<angle<0:
                turning -= 1
        return turning  

    def aligning(self, flockHeading, heading): # adjusts steering to go in heading flock
        turning = 0
        if heading > flockHeading:
            turning = 1
        else:
            turning = -1

        return turning
    
    def centring(self, flockPosition, heading): # asjust steering to the center of the flock
        turning =0
        
        angle = self.point.towards(flockPosition) - heading
        if angle > 180:
            angle -= 360
        elif angle < -180:
            angle += 360 
        
        if 0<angle< 180:
            turning = -1
        else:
            turning = 1

        return turning


#non class based functions

def twoPointAngle(oldPos, pos, bPoint): #finds the angle between two points,
    # it isn't very efficient and i have removed in all but 1 function.
    adx = pos[0] - bPoint[0]
    ady = pos[1] - bPoint[1]

    dx = oldPos[0]-pos[0]
    dy = oldPos[1]-pos[1]
      
    m1 = ady / adx
    m2 = dy / dx
    if  m1*m2 != -1:
        inpactAngle = math.degrees(math.atan((m2 - m1)/(1+m1*m2)))
    else:
        return 0
    
    return inpactAngle

def rotation(oldPos, pos): #uses two positions to find heading
    dx = oldPos[0]-pos[0]
    dy = oldPos[1]-pos[1]
      
    if dx != 0:
        rotation = math.degrees(math.atan(dy/dx))
    else:
        return 0

    if dx<0:
        if dy>0:
            rotation += 360
    elif dx>0:
        rotation += 180

    return rotation


def flockCenter(possitions): #gives Coordinates of the flock
    xList = []
    yList = []
    for point in possitions:
        xList.append(point[0])
        yList.append(point[1])
    
    x = sum(xList)/len(xList) 
    y = sum(yList)/len(yList)

    return x,y




# //////////MAIN CODE//////////////
circleSize = 100

    #circle setup
circle = turtle.Turtle()
circle.hideturtle()
circle.speed(0)
circle.penup()
circle.goto(0,-(circleSize))
circle.color("white")
circle.pendown()
circle.circle(circleSize)

# SETTING variables
numPoints = 8
    #flock creation
flock = []
for x in range(numPoints):
    flock.append(point(index = x))

possitions = []
oldPossitions = []

for point in flock:
    oldPossitions.append(point.point.pos())
    point.point.forward(1)

for point in flock:
    possitions.append(point.point.pos())
    point.point.forward(1)


#/////MAINLOOP/////
time = 0
while time < 500:
    #resetting position and heading variables
    for point in flock:
        oldPossitions[point.index] = possitions[point.index]
    
    for point in flock:
        possitions[point.index] = point.point.pos()
    
    #movement and steering
    for point in flock:
        point.movement(oldPossitions[point.index], possitions[point.index], circleSize)

        point.steering(flock = flock, possitions = possitions, oldPossitions = oldPossitions)
    
    time +=1



turtle.mainloop()
