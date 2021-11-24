#! /usr/bin/env python

import rospy
from std_msgs.msg import Int32 


class Subscriber():

    def __init__(self):

        self.sub = rospy.Subscriber('/counter', Int32, self.sub_callback)
        self.msg = Int32()


    def sub_callback(self, msg):

        self.msg = msg
        print(self.msg)


#Remember, for subscriber, you don't need to call the sub_callback function because once you start the subscriber, it will automatically start getting the value, so there is no need to further call the function
#and you can simply do as below, to further clarify this idea, you can compare it with maze_class.py as in that one we need to call the function as well. 
if __name__ == '__main__':

    rospy.init_node('topic_subscriber', anonymous=True)
    movebb8_object = Subscriber()
    rospy.spin()

   