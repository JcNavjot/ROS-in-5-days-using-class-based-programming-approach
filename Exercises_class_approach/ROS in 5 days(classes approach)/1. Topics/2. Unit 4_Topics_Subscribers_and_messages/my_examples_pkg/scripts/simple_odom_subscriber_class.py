#! /usr/bin/env python

import rospy
from nav_msgs.msg import Odometry 


class Subscriber():

    def __init__(self):

        self.sub = rospy.Subscriber('/odom', Odometry, self.sub_callback)
        self.msg = Odometry()
        

    def sub_callback(self, msg):

        
        #self.msg = msg.header  #This will print the header section of the Odometry message
        #self.msg = msg.pose  #This will print the pose section of the Odometry message
        self.msg = msg
        print(self.msg)


#Approach 1 using if name == main
if __name__ == '__main__':

    rospy.init_node('topic_subscriber', anonymous=True)
    movebb8_object = Subscriber()
    rospy.spin()

#Approach 2 without name == main

#rospy.init_node('topic_subscriber', anonymous=True)
#movebb8_object = Subscriber()
#movebb8_object.sub_callback(10)
#rospy.spin()


