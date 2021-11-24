#! /usr/bin/env python

import rospy
from my_custom_srv_msg_pkg.srv import MyCustomServiceMessage, MyCustomServiceMessageResponse
from geometry_msgs.msg import Twist

class SimpleCustomServer():

    def __init__(self):

        rospy.init_node('service_server_custom')
        self.my_service = rospy.Service('/move_bb8_in_circle_custom', MyCustomServiceMessage, self.my_callback)
        self.cmd = Twist()
        self.vel_publish = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
        self.rate = rospy.Rate(1)

    def my_callback(self, request):

        
        rospy.loginfo("The Service move_bb8_in_circle has been called")
        self.cmd.linear.x = 0.2
        self.cmd.angular.z = 0.2
        i = 0
        while i <= request.duration: 
            
            self.vel_publish.publish(self.cmd)
            self.rate.sleep()
            i=i+1
        
        self.cmd.linear.x = 0.0
        self.cmd.angular.z = 0.0
        self.vel_publish.publish(self.cmd)
        rospy.loginfo("Finished service move_bb8_in_circle_custom")
        response = MyCustomServiceMessageResponse()
        response.success = True
        return response # the service Response class, in this case EmptyResponse


f1 = SimpleCustomServer()
rospy.loginfo("Service /move_bb8_in_circle_custom Ready")
rospy.spin()