#!/usr/bin/env python

import rospy
from geometry_msgs import Twist

if __name__ == '__main__':
	try:
		move()
	except rospy.ROSInterruptException:
		pass

def move():
	pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)
	rospy.init_node('move', anonymous=True)
	rate = rospy.Rate(10)
	while not rospy.is_shutdown():
		move = Twist()
		move.linear.x = 1.0
		move.angular.z = 1.0
		rospy.loginfo(move)
		pub.publish(move)
		rate.sleep()

