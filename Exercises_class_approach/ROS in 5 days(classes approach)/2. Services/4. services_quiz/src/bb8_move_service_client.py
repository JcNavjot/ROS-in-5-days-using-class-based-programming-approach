#! /usr/bin/env python

import rospkg
import rospy
from services_quiz.srv import BB8CustomServiceMessage, BB8CustomServiceMessageRequest # you import the service message python classes generated from Empty.srv.

rospy.init_node('bb8_call_node')
rospy.wait_for_service('/move_bb8_in_square_custom')
move_bb8_service = rospy.ServiceProxy('/move_bb8_in_square_custom', BB8CustomServiceMessage)
move_bb8_object = BB8CustomServiceMessageRequest()

"""
# BB8CustomServiceMessage
float64 side       # The distance of each side of the circle
int32 repetitions    # The number of times BB-8 has to execute the circle movement when the service is called
---
bool success         # Did it achieve it?
"""


move_bb8_object.side = 1.5
move_bb8_object.repetitions = 2
rospy.loginfo("Start Two Small Squares...")
result = move_bb8_service(move_bb8_object) # Send through the connection the path to the trajectory file to be executed
rospy.loginfo(str(result)) # Print the result given by the service called


move_bb8_object = BB8CustomServiceMessageRequest()
move_bb8_object.side = 4
move_bb8_object.repetitions = 1
rospy.loginfo("Start One Big Square...")
result = move_bb8_service(move_bb8_object)
# Print the result given by the service called
rospy.loginfo(str(result))

rospy.loginfo("END of Service call...")