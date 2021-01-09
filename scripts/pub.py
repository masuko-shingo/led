#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

if __name__ == "__main__":
    rospy.init_node("pub")
    pub = rospy.Publisher("pub_led", String, queue_size=60)
    rate = rospy.Rate(1)

    while not rospy.is_shutdown():
        print("Please insert either [ROS],[1],[0].")
        n = input()
        pub.publish(n)
        rate.sleep()

