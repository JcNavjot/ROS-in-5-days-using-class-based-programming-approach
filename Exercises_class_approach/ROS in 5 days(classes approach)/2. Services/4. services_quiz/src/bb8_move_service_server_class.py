#! /usr/bin/env python

import rospy
from services_quiz.srv import BB8CustomServiceMessage, BB8CustomServiceMessageResponse # you import the service message python classes generated from Empty.srv.
from geometry_msgs.msg import Twist
from math import pi

class BB8CustomServer():

    def __init__(self):

        rospy.init_node('service_server_custom_square')
        self.my_service = rospy.Service('/move_bb8_in_square_custom', BB8CustomServiceMessage, self.my_callback)
        self.cmd = Twist()
        self.vel_publish = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
        self.rate = rospy.Rate(1)
        
    
    def my_callback(self, request):

        rospy.loginfo("The Service move_bb8_in_square has been called")
        sides = request.side
        reps = request.repetitions
        self.moveBB8(reps, sides)
        rospy.loginfo("Finished service move_bb8_in_square_custom")
        response = BB8CustomServiceMessageResponse()
        response.success = True
        return response # the service Response class, in this case EmptyResponse

    
    def straight(self, sides):

        wait_time = float(sides/2)
        self.cmd.linear.x = 0.2
        self.vel_publish.publish(self.cmd)
        rospy.sleep(wait_time)
        self.cmd.linear.x = 0.0
        self.vel_publish.publish(self.cmd)
        rospy.sleep(wait_time)

    def rotate(self):

        self.cmd.angular.z = 0.2
        self.vel_publish.publish(self.cmd)
        rospy.sleep(8)
        self.cmd.angular.z = 0.0
        self.vel_publish.publish(self.cmd)
        rospy.sleep(1)


    def moveBB8(self, reps, sides):
        i = 0
        j = 0
        while i < reps:
            while j < 4:    
                self.straight(sides)
                self.rotate()
                j+=1
            i+=1
            j=0


f1 = BB8CustomServer()
rospy.loginfo("Service /move_bb8_in_square_custom_ready")
rospy.spin()
