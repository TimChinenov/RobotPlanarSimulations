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

def getSegments(self):
    return self.sgmentList

def getJointAngles(self):
    return self.Q

def getEndPosition(self):
    return self.p0T

def getEndRotation(self):
    return self.r0T

def getJointPositions(self):
    return self.P

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
            self.p0T = self.p0T + np.dot(self.r0T,segments[i].getLength())
            self.r0T = np.dot(self.r0T,rot(zeroConfig[i]))
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
            positions[0].append(int(i[0]))
            positions[1].append(int(i[1]))
        return positions
    
    def getJointPositionsxy(self):
        positions = []
        for i in self.P:
            templist = []
            templist.append(int(i[0]))
            templist.append(int(i[1]))
            positions.append(templist)
        return positions    
