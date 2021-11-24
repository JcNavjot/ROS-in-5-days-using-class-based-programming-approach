#! /usr/bin/env python

import rospy
from exercise_43.msg import Age #Import Age message from the exercise_33 package


class PublishAge():

    def __init__(self):

        self.pub = rospy.Publisher('/age_info', Age, queue_size=1)
        self.rate = rospy.Rate(2)
        self.age = Age()
        self.age.years = 5 #Fill the values of the message
        self.age.months = 10 #Fill the values of the message
        self.age.days = 21
    
    
    def AgeFunc(self): 

        while not rospy.is_shutdown():

            self.pub.publish(self.age) #Publish the message into the defined topic /age_info
            self.rate.sleep()




if __name__ == '__main__':
    rospy.init_node('publish_age_node', anonymous=True)
    movebb8_object = PublishAge()
    try:
        movebb8_object.AgeFunc()
    except rospy.ROSInterruptException:
        pass

