#!/usr/bin/env python
# BEGIN ALL
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist

def talker():
    pub = rospy.Publisher('jackal_velocity_controller/cmd_vel', Twist, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    velmsg = Twist()

    #Draw T
    for num in range(1,40):
        if rospy.is_shutdown():
            break

        velmsg.linear.x = .5
        velmsg.angular.z = 0

        rospy.loginfo(velmsg)
        pub.publish(velmsg)
        rate.sleep()

    for num in range(1,20):
        if rospy.is_shutdown():
            break

        velmsg.linear.x = 0
        velmsg.angular.z = 0.785

        rospy.loginfo(velmsg)
        pub.publish(velmsg)
        rate.sleep()

    for num in range(1,20):
        if rospy.is_shutdown():
            break

        velmsg.linear.x = .5
        velmsg.angular.z = 0

        rospy.loginfo(velmsg)
        pub.publish(velmsg)
        rate.sleep()

    for num in range(1,20):
        if rospy.is_shutdown():
            break

        velmsg.linear.x = 0
        velmsg.angular.z = 1.57

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
        talker()
    except rospy.ROSInterruptException:
        pass

