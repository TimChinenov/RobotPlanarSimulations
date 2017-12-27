import Segment as sg
import RobotArm as ra
import matplotlib.pyplot as plt
import numpy as np

def main():
    s1 = sg.Segment(1,0)
    s2 = sg.Segment(2,0)
    s3 = sg.Segment(1,0)
    
    segments = [s1,s2,s3]
    zeroConfig = [np.pi/4,-np.pi/4,0]
    
    r1 = ra.RobotArm(segments,zeroConfig)
    
    print ShowArm(r1)

def ShowArm(arm):
    pos = arm.getJointPositions()
    plt.plot(pos[0],pos[1],'-ro')
    plt.axis([-5, 5, -5, 5])
    plt.show()
    return arm.getJointPositionsxy()


if __name__=="__main__":
    print "Starting Robot Arm"
    main()
