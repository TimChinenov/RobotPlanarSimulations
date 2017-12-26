import numpy as np

def rot(theta):
    #Function performs a 2-D matrix rotation based on theta
    R = np.matrix([np.cos(theta), (-1)*np.sin(theta)],
                    [np.sin(theta), np.cos(theta)])
    return R

def eye(val):
    #function creates val x val identity matrix
    ident = []
    for i in range(0,val):
        tempI = [0]*val;
        tempI[i] = 1;
        ident = ident.append(tempI);
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
    sgmentList = []; #List of segments
    numSegs = 0; #The number of segments this robot contains
    p0T = 0; #The vector from the origin to the end effector
    r0T = eye(3); #The rotation from the origin to the end effector
    Q = [] # List of joint angles
    P = [] #List of each joint position
    def __init__(self, segments, zeroConfig):
        for i in range(0:segments.length):
            p0T = p0T + r0T*segments(i).getLength()
            r0T = r0T*rot(zeroConfig(i))
            Q = Q.append(zeroConfig(i))
            P = P.append(p0T)

        numSegs = segments.length
        sgmentList = segments
