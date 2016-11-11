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

    dist = 2.0      #distance in meters
    time = 4      #time in seconds
    angle = 0       #angle in radians
    corr = 0        #correction to angle 
    for num in range(time * 10):
        if rospy.is_shutdown():
            break

        velmsg.linear.x = dist/time
        velmsg.angular.z = (angle+corr)/time

        rospy.loginfo(velmsg)
        pub.publish(velmsg)
        rate.sleep()


    dist = 0.0      #distance in meters
    time = 2        #time in seconds
    angle = -2.678  #angle in radians
    corr = -.19     #correction to angle 
    for num in range(time * 10):
        if rospy.is_shutdown():
            break

        velmsg.linear.x = dist/time
        velmsg.angular.z = (angle+corr)/time

        rospy.loginfo(velmsg)
        pub.publish(velmsg)
        rate.sleep()


    dist = math.sqrt(5)#distance in meters
    time = 4        #time in seconds
    angle = 0       #angle in radians
    corr = 0        #correction to angle 
    for num in range(time * 10):
        if rospy.is_shutdown():
            break

        velmsg.linear.x = dist/time
        velmsg.angular.z = (angle+corr)/time

        rospy.loginfo(velmsg)
        pub.publish(velmsg)
        rate.sleep()


    dist = 0.0      #distance in meters
    time = 2        #time in seconds
    angle = 2.2143  #angle in radians
    corr = .19      #correction to angle 
    for num in range(time * 10):
        if rospy.is_shutdown():
            break

        velmsg.linear.x = dist/time
        velmsg.angular.z = (angle+corr)/time

        rospy.loginfo(velmsg)
        pub.publish(velmsg)
        rate.sleep()


    dist = math.sqrt(5)#distance in meters
    time = 4        #time in seconds
    angle = 0       #angle in radians
    corr = 0        #correction to angle 
    for num in range(time * 10):
        if rospy.is_shutdown():
            break

        velmsg.linear.x = dist/time
        velmsg.angular.z = (angle+corr)/time

        rospy.loginfo(velmsg)
        pub.publish(velmsg)
        rate.sleep()

    dist = 0.0      #distance in meters
    time = 2        #time in seconds
    angle = -2.678  #angle in radians
    corr = -.29     #correction to angle 
    for num in range(time * 10):
        if rospy.is_shutdown():
            break

        velmsg.linear.x = dist/time
        velmsg.angular.z = (angle+corr)/time

        rospy.loginfo(velmsg)
        pub.publish(velmsg)
        rate.sleep()

    dist = 2.0      #distance in meters
    time = 4      #time in seconds
    angle = 0       #angle in radians
    corr = 0        #correction to angle 
    for num in range(time * 10):
        if rospy.is_shutdown():
            break

        velmsg.linear.x = dist/time
        velmsg.angular.z = (angle+corr)/time

        rospy.loginfo(velmsg)
        pub.publish(velmsg)
        rate.sleep()


  
if __name__ == '__main__':
    try:
        letterM()
    except rospy.ROSInterruptException:
        pass

