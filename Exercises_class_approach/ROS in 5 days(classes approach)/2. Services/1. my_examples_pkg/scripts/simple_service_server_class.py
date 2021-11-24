#! /usr/bin/env python

import rospy
from std_srvs.srv import Empty, EmptyResponse # you import the service message python classes generated from Empty.srv.
from geometry_msgs.msg import Twist

class SimpleServer():

    def __init__(self):

        rospy.init_node('service_server')
        self.my_service = rospy.Service('/my_service', Empty , self.my_callback)

    def my_callback(self):

        print("Your_callback has been called")
        return EmptyResponse() # the service Response class, in this case EmptyResponse
        #return MyServiceResponse(len(request.words.split())) 


if __name__ == '__main__':

    f1 = SimpleServer()
    try:
        f1.my_callback()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
    

#f1 = SimpleServer()
#f1.my_callback()
#rospy.spin()


#if __name__ == '__main__':

 #   f1 = SimpleServer()
  #      f1.my_callback()
   #     rospy.spin()
  #  except rospy.ROSInterruptException:
   #     pass
