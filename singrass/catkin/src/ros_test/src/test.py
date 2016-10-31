#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist

def test():
  pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
  rospy.init_node('test', anonymous = True)
  rate = rospy.Rate(10)
  move = Twist()

  while not rospy.is_shutdown():
    move.linear.x = 1.0
    move.linear.y = 0.0
    move.linear.z = 0.0
    move.angular.x = 0.0
    move.angular.y = 0.0
    move.angular.z = 0.0


    pub.publish(move)
    rate.sleep()

if __name__ == '__main__':
  try:
    test()
  except rospy.ROSInterruptException:
    pass

