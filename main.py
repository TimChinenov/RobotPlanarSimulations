#######################
#Current bugs:
#Need to delete existing robot 
#######################
import Segment as sg
import RobotArm as ra
import Window as win
import matplotlib.pyplot as plt
import numpy as np
from Tkinter import *

#Call the main program
def main():
    ################# Robot Stuff #####################
    #Declare the segments the robot arm will contain
    #Can have more than this many segments.
    s1 = sg.Segment(1,0)
    s2 = sg.Segment(1,0)
    s3 = sg.Segment(1,0)
    
    #Place segments into a list, this list is used to initialize the robot arm
    segments = [s1,s2,s3]
    #Declare the angle configurations of the arm.
    angleConfig = [0,0,0]
    
    
    
    ################ Canvas Stuff ####################
    #configure height and width for canvas
    wid = 640
    hei = 480
    scale = 50
    
    master = Tk()
    master.title = "ArmSim"
    vas = Canvas(master,width = wid, height = hei)
    vas.configure(background='white')
    #Canvas does not respond to keyboard commands if it is not focused on
    #So this important
    vas.focus_set() 
    vas.pack()
    
    drawGrid(vas,hei,wid,scale)
    
    r1 = ra.RobotArm(segments,angleConfig,vas)
    r1.drawArm()
    master.mainloop()
    return
##################################################################    
##################################################################    
##################################################################    
##################################################################    
    
def drawGrid(C,hei,wid,scale):
    #Draw the x-axis and y-axis
    C.create_line(wid/2,0,wid/2,hei, fill="black",width=1)
    C.create_line(0,hei/2,wid,hei/2, fill="black",width=1)
    Hcounts = int(round(hei/(2.0*scale)))
    Wcounts = int(round(wid/(2.0*scale))) 
    #Draw the intervals on the lines
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
        
def ShowArm(arm,C):
    scale = 50
    pos = arm.getJointPositionsxy()
    #Draw the actual segments of the robot
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
    #Draw the joint positions
    pos = arm.getJointPositionsxy()    
    for i in range(0,len(pos)):
        spot = pos[i]
        
        spot[0] = spot[0]*scale
        spot[1] = spot[1]*scale        
        
        spot = pixCoor(spot[0],spot[1],640,480)
        C.create_oval(spot[0]-5,spot[1]-5,spot[0]+5,spot[1]+5,fill="black") 
        
def pixCoor(x,y,width,height):
    u = x + width/2.0
    v = height/2.0 - y
    return [u,v]         
        

#The main function.
if __name__=="__main__":
    print "Starting Robot Arm"
    
    main()
