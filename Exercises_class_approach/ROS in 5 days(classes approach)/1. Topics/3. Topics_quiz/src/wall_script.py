#! /usr/bin/env python

import rospy
from robot_control_class import RobotControl
from geometry_msgs.msg import Twist
import time 

class TurtleBotWall():

    def __init__(self):

        self.rc = RobotControl()
        #self.ctrl_c = False
        self.rate = rospy.Rate(10)

    def stop_robot(self):

        self.rc.stop_robot()
    
    
    def move_straight(self):

       self.rc.move_straight()


    def move_left(self):

        self.rc.move_left()

    def move_right(self):

        self.rc.move_right()

    def AvoidWall(self):

        i = self.rc.get_front_laser()
        

        while True:
            
            if (i > 1):
                self.move_straight()
                i = self.rc.get_front_laser()
                print ("Current distance to wall: %f" % i)

            elif (i < 1):

                self.move_left()
                i = self.rc.get_front_laser()
                print ("Current distance to wall: %f" % i)
                time.sleep(3)
                self.stop_robot()
                break

        j = self.rc.get_laser(0) #right
        k = self.rc.get_laser(719) #left

        while True:
            
            if (j < 1):

                self.rc.turn_left()
                j = self.rc.get_laser(0)
                #print ("Current distance to wall: %f" % j)
                time.sleep(1)
                print ("Current distance to wall: %f" % i)
                self.stop_robot()
                
            
            if (k < 1):
                
                self.rc.turn_right()
                k = self.rc.get_laser(719)
                #print ("Current distance to wall: %f" % k)
            
            break


        self.move_straight()


f1 = TurtleBotWall()
f1.AvoidWall()
