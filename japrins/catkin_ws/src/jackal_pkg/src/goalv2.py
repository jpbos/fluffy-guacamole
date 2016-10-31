#!/usr/bin/env python
# BEGIN ALL
import rospy
from std_msgs.msg import String
import actionlib
from move_base_msgs.msg import MoveBaseGoal
from move_base_msgs.msg import MoveBaseAction
def goalv2():
        pub = rospy.Publisher('move_base', MoveBaseGoal,queue_size=10)
        rospy.init_node('goalset', anonymous=True)
        rate = rospy.Rate(10) # 10hz
        while not rospy.is_shutdown():

           goal = MoveBaseGoal()

           goal.target_pose.header.frame_id = "base_link"
           goal.target_pose.header.stamp = rospy.Time.now()

  	   goal.target_pose.pose.position.x = 1.0
           goal.target_pose.pose.orientation.w = 1.0

	   server = actionlib.SimpleActionServer('goalset', MoveBaseAction, goal, false)
           rospy.loginfo(goal)
           pub.publish(goal)
           rate.sleep()
   
if __name__ == '__main__':
       try:
          goalv2()
       except rospy.ROSInterruptException:
          pass

