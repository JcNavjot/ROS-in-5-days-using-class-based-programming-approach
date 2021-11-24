#! /usr/bin/env python

import rospy
from std_srvs.srv import Empty, EmptyResponse # you import the service message python classes generated from Empty.srv.
from geometry_msgs.msg import Twist

class SimpleServer():

    def __init__(self):

        rospy.init_node('service_server')
        self.my_service = rospy.Service('/move_bb8_in_circle', Empty , self.my_callback)
        self.cmd = Twist()
        self.vel_publish = rospy.Publisher('/cmd_vel', Twist, queue_size=1)


    def my_callback(self, request):

        rospy.loginfo("The Service move_bb8_in_circle has been called")
        self.cmd.linear.x = 0.0
        self.cmd.angular.z = 0.0
        self.vel_publish.publish(self.cmd)
        rospy.loginfo("Finished service move_bb8_in_circle")
        return EmptyResponse() # the service Response class, in this case EmptyResponse


f1 = SimpleServer()
rospy.loginfo("Service /move_bb8_in_circle Ready")
rospy.spin()


#f1 = SimpleServer()
#rospy.spin()
