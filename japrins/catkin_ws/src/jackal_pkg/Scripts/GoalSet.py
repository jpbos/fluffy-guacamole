#!/usr/bin/env python
# BEGIN ALL
import rospy
import move_base_msgs.msg 
from nav_msgs.msg import Odometry
from geometry_msgs.msg import *
from tf.msg import


def GoalSet():
        pub = rospy.Publisher('move_base_simple/goal', PoseStamped, queue_size=1)
        rospy.init_node('GoalSet', anonymous=True)
        rate = rospy.Rate(10) 
	c =0;
        while not c ==4:

           	goal = PoseStamped()
 	   	goal.header.frame_id = "base_link";
           	goal.header.stamp = rospy.Time.now();
	   	goal.pose.position.x = 5.0; #meters
	   	goal.pose.orientation.z = .707; #radians
		goal.pose.orientation.w = .707;

           	rospy.loginfo(goal)
           	pub.publish(goal)
		c=c +1;
           	rate.sleep()
def VelCorrect();
	pub = rospy.Publisher('/jackal_velocity_controller/cmd_vel', Twist)
	rospy.init_node('VelCorrect',anonymous = True)
	rate = rospy.Rate(10)

	while not c =1

		goal = Twist()
	   	goal.orientation.z = .707; #Quarterions
		goal.orientation.w = .707; #Quarterions
           	rospy.loginfo(goal)
           	pub.publish(goal)

		if orient.z = .707 & orient.w = .707
			c = 1;

def listener():
	rospy.init_node('listener', anonymous=True)
	rospy.Subscriber("/odometry/filtered", String, callback)

    	rospy.spin()		
   	
if __name__ == '__main__':
       try:
          GoalSet()
	  VelCorrect()
       except rospy.ROSInterruptException:
          pass

