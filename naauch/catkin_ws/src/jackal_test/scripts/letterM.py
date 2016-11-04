#!/usr/bin/env python
# BEGIN ALL
import rospy
import math
from std_msgs.msg import String
from geometry_msgs.msg import Twist

def letterM():
    pub = rospy.Publisher('jackal_velocity_controller/cmd_vel', Twist, queue_size=10)
    rospy.init_node('letterM', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    velmsg = Twist()
    pi = math.pi

    for num in range(1,40):
        if rospy.is_shutdown():
            break

        velmsg.linear.x = .5
        velmsg.angular.z = 0

        rospy.loginfo(velmsg)
        pub.publish(velmsg)
        rate.sleep()
           
    for num in range(1,14):
        if rospy.is_shutdown():
            break

        velmsg.linear.x = 0
        velmsg.angular.z = -2

        rospy.loginfo(velmsg)
        pub.publish(velmsg)
        rate.sleep()

    for num in range(1,44):
        if rospy.is_shutdown():
            break

        velmsg.linear.x = .5
        velmsg.angular.z = 0

        rospy.loginfo(velmsg)
        pub.publish(velmsg)
        rate.sleep()

    for num in range(1,10):
        if rospy.is_shutdown():
            break

        velmsg.linear.x = 0
        velmsg.angular.z = 2

        rospy.loginfo(velmsg)
        pub.publish(velmsg)
        rate.sleep()

    for num in range(1,44):
        if rospy.is_shutdown():
            break

        velmsg.linear.x = .5
        velmsg.angular.z = 0

        rospy.loginfo(velmsg)
        pub.publish(velmsg)
        rate.sleep()

    for num in range(1,15):
        if rospy.is_shutdown():
            break

        velmsg.linear.x = 0
        velmsg.angular.z = -2

        rospy.loginfo(velmsg)
        pub.publish(velmsg)
        rate.sleep()

    for num in range(1,40):
        if rospy.is_shutdown():
            break

        velmsg.linear.x = .5
        velmsg.angular.z = 0

        rospy.loginfo(velmsg)
        pub.publish(velmsg)
        rate.sleep()

    
         
  
if __name__ == '__main__':
    try:
        letterM()
    except rospy.ROSInterruptException:
        pass

