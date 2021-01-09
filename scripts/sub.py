#!/usr/bin/env python3

import rospy
import time
from std_msgs.msg import String

def cb(msg):
    global i
    if msg.data == 'ROS':
        print("R O S")
        print(".-. --- ...")
        time.sleep(0.5)
        #R
        with open("/dev/myled0", "w") as f:
            f.write("1\n" )
        time.sleep(0.2)
        with open("/dev/myled0", "w") as f:
            f.write("0\n" )
        time.sleep(0.2)

        with open("/dev/myled0", "w") as f:
            f.write("1\n" )
        time.sleep(0.5)
        with open("/dev/myled0", "w") as f:
            f.write("0\n" )
        time.sleep(0.5)

        with open("/dev/myled0", "w") as f:
            f.write("1\n" )
        time.sleep(0.2)
        with open("/dev/myled0", "w") as f:
            f.write("0\n" )
        time.sleep(0.2)

        time.sleep(0.1)

        for i in range(3):    #O
            with open("/dev/myled0", "w") as f:
                f.write("1\n" )
            time.sleep(0.5)
            with open("/dev/myled0", "w") as f:
                f.write("0\n" )
            time.sleep(0.5)
                
        time.sleep(0.1)

        for i in range(3):    #S
            with open("/dev/myled0", "w") as f:
                f.write("1\n" )
            time.sleep(0.2)
            with open("/dev/myled0", "w") as f:
                f.write("0\n" )
            time.sleep(0.2)

    if msg.data == '1':
        print("on")
        with open("/dev/myled0", "w") as f:
            f.write("1\n" )
    if msg.data == '0':
        print("off")
        with open("/dev/myled0", "w") as f:
            f.write("0\n" )
    else:
        print(" ")

if __name__ == "__main__":
    rospy.init_node("sub")
    sub = rospy.Subscriber("pub_led", String, cb)
    rospy.spin()

