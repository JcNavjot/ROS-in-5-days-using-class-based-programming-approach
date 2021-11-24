#! /usr/bin/env python

import rospy
import actionlib
from actionlib.msg import TestFeedback, TestResult, TestAction
import time
from geometry_msgs.msg import Twist
from std_msgs.msg import Empty

class MoveDroneSquareClass(object):
    
  # create messages that are used to publish feedback/result
    _feedback = TestFeedback()
    _result   = TestResult()

    def __init__(self):
    # creates the action server
        self._ss = actionlib.SimpleActionServer("drone_square_server", TestAction, self.goal_callback, False)
        self._ss.start()
        self._cmd_vel = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
        self._move_msg = Twist()
        self._pub_takeoff = rospy.Publisher('/drone/takeoff', Empty, queue_size=1)
        self._takeoff_msg = Empty()
        self._pub_land = rospy.Publisher('/drone/land', Empty, queue_size=1)
        self._land_msg = Empty()
        self.ctrl_c = False
        self.rate = rospy.Rate(10)

    def publish_once_in_cmd_vel(self, cmd):
        """
        This is because publishing in topics sometimes fails teh first time you publish.
        In continuos publishing systems there is no big deal but in systems that publish only
        once it IS very important.
        """
        while not self.ctrl_c:
            connections = self._cmd_vel.get_num_connections()
            if connections > 0:
                self._cmd_vel.publish(cmd)
                rospy.loginfo("Publish in cmd_vel...")
                break
            else:
                self.rate.sleep()

    def move_straight(self):

        rospy.loginfo("Moving forward ...")
        self._move_msg.linear.x = 1.0
        self._move_msg.angular.z = 0.0
        self.publish_once_in_cmd_vel(self._move_msg)

    def rotate_drone(self):

        rospy.loginfo("Rotating ...")
        self._move_msg.linear.x = 0.0
        self._move_msg.angular.z = 1.0
        self.publish_once_in_cmd_vel(self._move_msg)
  
    def stop_drone(self):

        rospy.loginfo("Stopping ...")
        self._move_msg.linear.x = 0.0
        self._move_msg.angular.z = 1.0
        self.publish_once_in_cmd_vel(self._move_msg)
  
  
    def goal_callback(self, goal):
    # this callback is called when the action server is called.
    # this is the function that computes the Fibonacci sequence
    # and returns the sequence to the node that called the action server
    # helper variables
        r = rospy.Rate(1)
        success = True

    # Now make the drone takeoff
    
        i = 0
        while not i == 3:

            self._pub_takeoff.publish(self._takeoff_msg)
            rospy.loginfo('Taking off...')
            time.sleep(1)
            i+=1
 
    # Now you need to define the goal as it will be used in the upcoming main function

        sideSeconds = goal.goal
        turnSeconds = 1.8
    
        i = 0
        for i in range(0, 4):
    
      # check that preempt (cancelation) has not been requested by the action client
            if self._ss.is_preempt_requested():
                rospy.loginfo('The goal has been cancelled/preempted')
        # the following line, sets the client in preempted state (goal cancelled)
                self._ss.set_preempted()
                success = False
        # we end the calculation of the Fibonacci sequence
                break

            self.move_straight()
            time.sleep(sideSeconds)
            self.rotate_drone()
            time.sleep(turnSeconds)
    
        # Now comes the feedback part which actually makes action program different from the other ones, once feedback is done, then result is left
        # first feedback, then result
        # Feedback comes in main function loop because it is published again and again

        # build and publish the feedback message
            self._feedback.feedback = i
            self._ss.publish_feedback(self._feedback)
      # the sequence is computed at 1 Hz frequency
            r.sleep()

    # at this point, either the goal has been achieved (success==true)
    # or the client preempted the goal (success==false)
    # If success, then we publish the final result
    # If not success, we do not publish anything in the result
        if success:
            self._result.result = (turnSeconds*4) + (sideSeconds*4)
            rospy.loginfo('The total seconds it took the drone to perform the square was %i' % self._result.result)
            self._ss.set_succeeded(self._result)
      

     # make the drone stop and land
            self.stop_drone()
            i=0
            while not i == 3:
                self._pub_land.publish(self._land_msg)
                rospy.loginfo('Landing...')
                time.sleep(1)
                i += 1

      
if __name__ == '__main__':

    rospy.init_node('move_square')
    MoveDroneSquareClass()
    rospy.spin()