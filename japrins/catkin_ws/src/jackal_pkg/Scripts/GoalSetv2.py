#!/usr/bin/env python
# BEGIN ALL
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import PoseStamped
import move_base_msgs.msg 

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
	   	goal.pose.orientation.z = 1.5708; #radians

           	rospy.loginfo(goal)
           	pub.publish(goal)
		c=c +1;
           	rate.sleep()
           
   	
if __name__ == '__main__':
       try:
          GoalSet()
       except rospy.ROSInterruptException:
          pass

