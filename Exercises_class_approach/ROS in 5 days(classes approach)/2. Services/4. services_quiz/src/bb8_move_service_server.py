#! /usr/bin/env python

import rospy
from services_quiz.srv import BB8CustomServiceMessage, BB8CustomServiceMessageResponse # you import the service message python classes generated from Empty.srv.
from geometry_msgs.msg import Twist
from math import pi

def my_callback(request):
    my_response = BB8CustomServiceMessageResponse()
    sides = request.side
    reps = request.repetitions
    moveBB8(reps, sides)
    my_response.success = True
    return my_response.success

def straight(sides):
    wait_time = float(sides/2)
    move.linear.x = 0.3
    pub.publish(move)
    rospy.sleep(wait_time)
    move.linear.x = 0.0
    pub.publish(move)
    rospy.sleep(wait_time)

def rotate():
    move.angular.z = 0.2
    pub.publish(move)
    rospy.sleep(8)
    move.angular.z = 0
    pub.publish(move)
    rospy.sleep(1)

def moveBB8(reps, sides):
    i = 0
    j = 0
    while i < reps:
        while j < 4:    
            straight(sides)
            rotate()
            j+=1
        i+=1
        j=0



    #move.linear.x = 0
    #move.angular.z = 0
    #pub.publish(move)
    rospy.loginfo("Finished service move_bb8_in_square_custom")
    
    #response = BB8CustomServiceMessageResponse()
    #response.success = True
    #return response # the service Response class, in this case EmptyResponse
rospy.init_node('bb8_square_node') 
my_service = rospy.Service('/move_bb8_in_square_custom', BB8CustomServiceMessage , my_callback) # create the Service called my_service with the defined callback
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=2)
move = Twist()
rate = rospy.Rate(1)
rospy.spin() # maintain the service open.

