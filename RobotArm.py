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

class RobotArm:
    sgmentList = [] #List of segments
    numSegs = 0 #The number of segments this robot contains
    p0T = np.matrix([[0],[0]]) #The vector from the origin to the end effector
    r0T = eye(2) #The rotation from the origin to the end effector
    Q = [] # List of joint angles
    P = [] #List of each joint position
    def __init__(self, segments, zeroConfig):
        self.P.append(self.p0T)
        for i in range(0,len(segments)):
            self.r0T = np.dot(self.r0T,rot(zeroConfig[i]))            
            self.p0T = self.p0T + np.dot(self.r0T,segments[i].getLength())
            (self.Q).append(zeroConfig[i])
            (self.P).append(self.p0T)
            

        numSegs = len(segments)
        sgmentList = segments
        
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
        self.p0T = np.matrix([[0],[0]]) #The vector from the origin to the end effector
        self.r0T = eye(2) #The rotation from the origin to the end effector
        self.P = [] #List of each joint position
        
        self.P.append(self.p0T)
        for i in range(0,numSegs):
            self.r0T = np.dot(self.r0T,rot(zeroConfig[i]))            
            self.p0T = self.p0T + np.dot(self.r0T,segments[i].getLength())
            (self.Q).append(zeroConfig[i])
            (self.P).append(self.p0T)        
        
        
    
