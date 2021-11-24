#! /usr/bin/env python

import rospy
from geometry_msgs.msg import Twist

class TurtleBotWall():

    def __init__(self):

        self.pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
        self.cmd = Twist()
        self.rate = rospy.Rate(1)
        self.ctrl_c = False


    def stop(self):

        self.cmd.linear.x = 0.0
        self.cmd.angular.z = 0.0
        self.pub.publish(self.cmd)
        self.rate.sleep()
    
    
    def MoveWall(self):

        i = 0
        while i<4: 
            self.cmd.linear.x = 0.1
            self.cmd.angular.z = 0.1
            self.pub.publish(self.cmd)
            self.rate.sleep()
            i+=1
        
        self.stop()


if __name__ == '__main__':
    rospy.init_node('move_turtlebot', anonymous=True)
    movebb8_object = TurtleBotWall()
    try:
        movebb8_object.MoveWall()
    except rospy.ROSInterruptException:
        pass
























