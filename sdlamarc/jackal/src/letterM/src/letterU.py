#!/usr/bin/env python
import rospy
import math
from geometry_msgs.msg import Twist

pub = rospy.Publisher('cmd_vel', Twist, queue_size=1)
rospy.init_node('letterU')

twist = Twist()

stage_change_time = rospy.Time.now()
rate = rospy.Rate(50)

stage = -1

while not rospy.is_shutdown():
    twist.linear.x = 0
    twist.angular.z = 0
    if stage == 1:
        twist.linear.x = 1
    if stage == 2:
        twist.angular.z = math.pi/6
    if stage == 3:
        twist.linear.x = 0.5
    if stage == 4:
        twist.angular.z = math.pi/6
    if stage == 5:
        twist.linear.x = 1
    pub.publish(twist)
    if rospy.Time.now() >= stage_change_time:
        stage += 1
        stage_change_time = rospy.Time.now() + rospy.Duration(3)
    rate.sleep()
