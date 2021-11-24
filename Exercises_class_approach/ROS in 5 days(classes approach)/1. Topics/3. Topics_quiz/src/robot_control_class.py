#! /usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan
import time

class RobotControl():

    def __init__(self):
        
        rospy.init_node('topics_quiz_node', anonymous=True)
        self.laser_subscriber = rospy.Subscriber('/kobuki/laser/scan', LaserScan, self.laser_callback)
        self.vel_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
        self.cmd = Twist()
        self.msg = LaserScan()
        self.rate = rospy.Rate(1) # This helps reduce the speed of readings taken from subscriber.
        self.ctrl_c = False
    
    
    def publish_once_in_cmd_vel(self):
        """
        This is because publishing in topics sometimes fails the first time you publish.
        In continuous publishing systems, this is no big deal, but in systems that publish only
        once, it IS very important.
        """
        while not self.ctrl_c:
            connections = self.vel_publisher.get_num_connections()
            if connections > 0:
                self.vel_publisher.publish(self.cmd)
                #rospy.loginfo("Cmd Published")
                break
            else:
                self.rate.sleep()
    
    
    # This function is used for subscriber
    def laser_callback(self, msg):

        self.laser_msg = msg  #Here you need to define which part of the message from the subscriber you want to use in all the other functions. 
        
        #print(self.laser_msg)
    
    def get_laser_full(self):

        time.sleep(1)
        return self.laser_msg.ranges  # Then from here, you can now use the msg defined in the laser_callback for any function you want, the laser_callback is the main function from the subscriber and once that is defined using self.msg = msg, then you can now use it in any function

    def get_front_laser(self):

        time.sleep(1)
        return self.laser_msg.ranges[360]

    def get_laser(self, pos):

        time.sleep(1)
        return self.laser_msg.ranges[pos]
    
    def stop_robot(self):

        time.sleep(1)
        self.cmd.linear.x = 0.0
        self.cmd.linear.y = 0.0
        self.cmd.linear.z = 0.0
        self.cmd.angular.x = 0.0
        self.cmd.angular.y = 0.0
        self.cmd.angular.z = 0.0
        self.publish_once_in_cmd_vel()  

    
    def move_straight(self):

        self.cmd.linear.x = 0.3
        self.publish_once_in_cmd_vel()

    def move_left(self):

        self.cmd.linear.x = 0.1
        self.cmd.linear.y = 0.0
        self.cmd.linear.z = 0.0
        self.cmd.angular.x = 0.0
        self.cmd.angular.y = 0.0
        self.cmd.angular.z = 0.3
        self.publish_once_in_cmd_vel()

    def turn_left(self):

        self.cmd.linear.x = 0.0
        self.cmd.linear.y = 0.0
        self.cmd.linear.z = 0.0
        self.cmd.angular.x = 0.0
        self.cmd.angular.y = 0.0
        self.cmd.angular.z = 0.3
        self.publish_once_in_cmd_vel()

    def move_right(self):

        self.cmd.linear.x = 0.1
        self.cmd.linear.y = 0.0
        self.cmd.linear.z = 0.0
        self.cmd.angular.x = 0.0
        self.cmd.angular.y = 0.0
        self.cmd.angular.z = -0.3
        self.publish_once_in_cmd_vel()


if __name__ == '__main__':

    robotcontrol_object = RobotControl()
    try:
        robotcontrol_object.move_straight()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
    
