#!/usr/bin/env python
# BEGIN ALL
import rospy
import math
from std_msgs.msg import String
from geometry_msgs.msg import Twist

def talker():
    pub = rospy.Publisher('jackal_velocity_controller/cmd_vel', Twist, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    velmsg = Twist()
    pi = math.pi

    angle = pi/2    #in radians
    time = 1        #in seconds
    distance = 0    #in meters
    for num in range(time * 12):
        if rospy.is_shutdown():
            break

        velmsg.linear.x = distance/time
        velmsg.angular.z = angle/time

        rospy.loginfo(velmsg)
        pub.publish(velmsg)
        rate.sleep()    
         
  
if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass

