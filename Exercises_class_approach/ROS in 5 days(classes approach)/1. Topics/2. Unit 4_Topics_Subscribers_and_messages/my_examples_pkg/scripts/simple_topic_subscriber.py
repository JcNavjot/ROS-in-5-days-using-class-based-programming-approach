#! /usr/bin/env python

import rospy                                          
from std_msgs.msg import Int32 

def callback(msg):                                    # Define a function called 'callback' that receives a parameter 
                                                      # named 'msg'
  
    print (msg)                                  # Print the value 'data' inside the 'msg' parameter

rospy.init_node('topic_subscriber')                   # Initiate a Node called 'topic_subscriber'

sub = rospy.Subscriber('/counter', Int32, callback)   # Create a Subscriber object that will listen to the /counter
                                                      # topic and will cal the 'callback' function each time it reads
                                                      # something from the topic
rospy.spin()              