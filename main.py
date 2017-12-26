import Segment
import RobotArm
import matplotlib.pyplot as plt

def main():
    s1 = Segment(1,0)
    s2 = Segment(1,0)
    s3 = Segment(1,0)
    segments = [s1,s2,s3]
    zeroConfig = [0,0,0]
    r1 = RobotArm(segments,zeroConfig)
    ShowArm(r1)

def ShowArm(arm):
    positions = arm.getJointPositions()




if _name__=="__main_":
    main()
