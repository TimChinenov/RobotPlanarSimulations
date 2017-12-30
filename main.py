import Segment as sg
import RobotArm as ra
from Tkinter import *
import matplotlib.pyplot as plt
import numpy as np

#Call the main program
def main():
    #Declare the segments the robot arm will contain
    #Can have more than this many segments.
    s1 = sg.Segment(2.5,0)
    s2 = sg.Segment(1,0)
   # s3 = sg.Segment(1,0)
    
    #Place segments into a list, this list is used to initialize the robot arm
    segments = [s1,s2]
    #Declare the angle configurations of the arm.
    angleConfig = [0,np.pi/4]
    
    r1 = ra.RobotArm(segments,angleConfig)
    #configure height and width for canvas
    wid = 640
    hei = 480
    scale = 50
    
    #call Tkinter
    master = Tk()
    
    #Make a canvas that will be drawn on
    vas = Canvas(master,width = wid, height = hei)
    vas.configure(background='white')
    vas.pack()
    #vas.bind(
    drawGrid(vas,hei,wid,scale)
    
    #populate the canvas with the robotic arm
    print ShowArm(r1,vas)
    #hold the canvas
    mainloop()
    

#function takes arm and a canvas and draws the arm on the canvas
def ShowArm(arm,C):
    scale = 50
    pos = arm.getJointPositionsxy()
    for i in range(0,len(pos)-1):
        pos = arm.getJointPositionsxy()
        s = pos[i]
        
        s[0] = s[0]*scale
        s[1] = s[1]*scale
        
        e = pos[i+1]
        
        e[0] = e[0]*scale
        e[1] = e[1]*scale
        
        s = pixCoor(s[0],s[1],640,480)
        e = pixCoor(e[0],e[1],640,480)
        print e
        C.create_line(s[0], s[1], e[0], e[1], fill="green",width=3)

    pos = arm.getJointPositionsxy()    
    for i in range(0,len(pos)):
        spot = pos[i]
        
        spot[0] = spot[0]*scale
        spot[1] = spot[1]*scale        
        
        spot = pixCoor(spot[0],spot[1],640,480)
        C.create_oval(spot[0]-5,spot[1]-5,spot[0]+5,spot[1]+5,fill="black")
    
        
    
#converts cartesian coordinates to pixel coordinates for the canvas to use.    
def pixCoor(x,y,width,height):
    u = x + width/2.0
    v = height/2.0 - y
    return [u,v]


def drawGrid(C,hei,wid,scale):
    C.create_line(wid/2,0,wid/2,hei, fill="black",width=1)
    C.create_line(0,hei/2,wid,hei/2, fill="black",width=1)
    Hcounts = int(round(hei/(2.0*scale)))
    Wcounts = int(round(wid/(2.0*scale))) 
    for i in range(0,Hcounts):
        pos = pixCoor(0,i*scale,640,480)
        C.create_line(wid/2-3,pos[1],wid/2+3,pos[1],fill="black")
        pos = pixCoor(0,-i*scale,640,480)
        C.create_line(wid/2-3,pos[1],wid/2+3,pos[1],fill="black")        
    for i in range(0,Wcounts):
        pos = pixCoor(i*scale,0,640,480)
        C.create_line(pos[0],hei/2+3,pos[0],hei/2-3,fill="black")
        pos = pixCoor(-i*scale,0,640,480)
        C.create_line(pos[0],hei/2+3,pos[0],hei/2-3,fill="black")
        
    

#The main function of the program.
if __name__=="__main__":
    print "Starting Robot Arm"
    #master = Tk()
    
    #w = Canvas(master, width=200, height=100)
    #w.pack()
    
    #w.create_line(0, 0, 200, 100)
    #w.create_line(0, 100, 200, 0, fill="red", dash=(4, 4))    
    main()
