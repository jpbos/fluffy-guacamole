#do not run as is
#just for storage of letters

#Draw M
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
