# RobotPlanarSimulations

This project demonstrates foward kinematics of planar robots.

The project contains a Three files:
main.py - This file handles the initialization of segments and the robot arm. This script should be run to receive an image of the robot that can be manipulated.
Segment.py - This file contains the class to make segment objects. Segments have a length. All segments are the same. Each Segment starts and ends with a revolute joint in the z-axis (out of the screen). 
RobotArm.py - This file contains the class RobotArm. RobotArm constructs the planar arm out of Segment objects. The class is also responsible for displaying the image of the robot and handing controls. 

Default Controls:
Each joint can be selected by inputting the appropriate number during run time. Because this, a robot cannot have more than 10 joints. The first joint is considered to be the 0th joint. To increase the joint angle press 'W' and to decrease the joint angle press 'S'.
