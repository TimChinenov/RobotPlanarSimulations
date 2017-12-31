from Tkinter import *
import Segment as sg
import RobotArm as ra

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
        
def pixCoor(x,y,width,height):
    u = x + width/2.0
    v = height/2.0 - y
    return [u,v] 

class Window:
    #configure height and width for canvas
    wid = 640
    hei = 480
    scale = 50   
        
    def __init__(self,arm):
        #call Tkinter
        self.master = Tk()
        self.master.title = "ArmSim"
        self.vas = Canvas(self.master,width = self.wid, height = self.hei)
        self.vas.configure(background='white')
        self.vas.pack()
        drawGrid(self.vas,self.hei,self.wid,self.scale)
        self.Arm = arm
        
        ShowArm(self.Arm,self.vas)
        self.vas.bind("<Key>",self.press)
        mainloop()
            
    def press(self,event):
        print "key pressed: " + repr(event)
    
        
        
        
        
    
   