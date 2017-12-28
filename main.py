import Segment as sg
import RobotArm as ra
from Tkinter import *
import matplotlib.pyplot as plt
import numpy as np

#Call the main program
def main():
    #Declare the segments the robot arm will contain
    #Can have more than this many segments.
    s1 = sg.Segment(1.5,0)
    s2 = sg.Segment(1,0)
    s3 = sg.Segment(0.75,0)
    
    #Place segments into a list, this list is used to initialize the robot arm
    segments = [s1,s2,s3]
    #Declare the angle configurations of the arm.
    angleConfig = [0,0,0]
    
    r1 = ra.RobotArm(segments,angleConfig)
    print ShowArm(r1)
    

def ShowArm(arm):
    pos = arm.getJointPositions()
    


def press(event):
    sys.stdout.flush()
    if (unicode(event.key,'utf-8')).isnumeric():
        jointSelect = int(unicode(event.key,'utf-8'))
        fig.canvas.draw()
    if event.key == 'up':
        print "roger"
        angles[jointSelect] == angles[jointSelect] + 1
    if event.key == 'down':
        angles[jointSelect] == angles[jointSelect] - 1

#The main function of the program.
if __name__=="__main__":
    print "Starting Robot Arm"
    master = Tk()
    
    w = Canvas(master, width=200, height=100)
    w.pack()
    
    w.create_line(0, 0, 200, 100)
    w.create_line(0, 100, 200, 0, fill="red", dash=(4, 4))    
    main()
