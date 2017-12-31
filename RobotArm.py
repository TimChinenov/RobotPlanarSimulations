import numpy as np
import Segment as sg

def rot(theta):
    #Function performs a 2-D matrix rotation based on theta
    R = np.matrix([[np.cos(theta), (-1)*np.sin(theta)],
                    [np.sin(theta), np.cos(theta)]])
    return R

def eye(val):
    #function creates val x val identity matrix
    ident = []
    for i in range(0,val):
        tempI = [0]*val
        tempI[i] = 1
        ident.append(tempI)
    identM = np.asarray(ident)
    return identM

def pixCoor(x,y,width,height):
    u = x + width/2.0
    v = height/2.0 - y
    return [u,v]     

class RobotArm:
    sgmentList = [] #List of segments
    numSegs = 0 #The number of segments this robot contains
    p0T = np.matrix([[0],[0]]) #The vector from the origin to the end effector
    r0T = eye(2) #The rotation from the origin to the end effector
    Q = [] # List of joint angles
    P = [] #List of each joint position
    focusedJoint = 0
    
    def __init__(self, segments, zeroConfig,canvas):
        self.focusedJoint = 0
        self.canvas = canvas
        self.drawnItems = []
        self.canvas.bind("<Key>", self.press)
        self.P.append(self.p0T)
        for i in range(0,len(segments)):
            self.r0T = np.dot(self.r0T,rot(zeroConfig[i]))            
            self.p0T = self.p0T + np.dot(self.r0T,segments[i].getLength())
            (self.Q).append(zeroConfig[i])
            (self.P).append(self.p0T)
            
           
        self.numSegs = len(segments)
        self.sgmentList = segments
        
        
    def drawArm(self):
        scale = 50
        pos = self.getJointPositionsxy()
        #Draw the actual segments of the robot
        for i in range(0,len(pos)-1):
            pos = self.getJointPositionsxy()
            s = pos[i]
            
            s[0] = s[0]*scale
            s[1] = s[1]*scale
            
            e = pos[i+1]
            
            e[0] = e[0]*scale
            e[1] = e[1]*scale
            
            s = pixCoor(s[0],s[1],640,480)
            e = pixCoor(e[0],e[1],640,480)
            print e
            self.drawnItems.append(self.canvas.create_line(s[0], s[1], e[0], e[1], fill="green",width=3))
        #Draw the joint positions
        pos = self.getJointPositionsxy()    
        for i in range(0,len(pos)):
            spot = pos[i]
            
            spot[0] = spot[0]*scale
            spot[1] = spot[1]*scale        
            
            spot = pixCoor(spot[0],spot[1],640,480)
            self.drawnItems.append(self.canvas.create_oval(spot[0]-5,spot[1]-5,spot[0]+5,spot[1]+5,fill="black"))
        return
            
    def press(self, event):
        if event.char.isdigit():
            print "number of segs: " + str(self.numSegs)
            print event.char
            if int(event.char) >= self.numSegs:
                self.focusedJoint = 0
            else:  
                self.focusedJoint = int(event.char)
        elif str(event.char) == "w":
            print "you pressed w"
            self.modJointAngle(self.focusedJoint,np.pi/180)
            self.clearLines()
            self.drawArm()
        elif str(event.char) == "s":
            print "you pressed s"
            self.modJointAngle(self.focusedJoint,-np.pi/180)
            self.clearLines()
            self.drawArm()
        else:
            print "That button does nothing"
        
    def clearLines(self):
        for item in self.drawnItems:
            self.canvas.delete(item)
        self.drawItems = []    
    def getSegments(self):
        return self.sgmentList
    
    def getJointAngles(self):
        return self.Q
    
    def getEndPosition(self):
        return self.p0T
    
    def getEndRotation(self):
        return self.r0T
    
    def getJointPositions(self):
        positions = [[],[]]
        for i in self.P:
            positions[0].append(float(i[0]))
            positions[1].append(float(i[1]))
        return positions
    
    def getJointPositionsxy(self):
        positions = []
        for i in self.P:
            templist = []
            templist.append(float(i[0]))
            templist.append(float(i[1]))
            positions.append(templist)
        return positions    
    
    #def setJointAngle(self,joint,angle):
    def modJointAngle(self,joint,mod):
        self.Q[joint] = self.Q[joint] + mod
        print self.Q
        self.p0T = np.matrix([[0],[0]]) #The vector from the origin to the end effector
        self.r0T = eye(2) #The rotation from the origin to the end effector
        self.P = [] #List of each joint position
        
        self.P.append(self.p0T)
        for i in range(0,self.numSegs):
            self.r0T = np.dot(self.r0T,rot(self.Q[i]))            
            self.p0T = self.p0T + np.dot(self.r0T,self.sgmentList[i].getLength())
            (self.P).append(self.p0T)
            
            
        
        
        
    
