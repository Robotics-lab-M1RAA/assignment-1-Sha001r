#!/usr/bin/python3

import rospy
from std_msgs.msg import String

def talker():
    rospy.init_node("Sharan_pubnode",anonymous=True)
    pub = rospy.Publisher("Greetings",String,queue_size=10)
    rate = rospy.Rate(10)
    msg = "Hello,I am Sharan"
    while not rospy.is_shutdown():
        pub.publish(msg)
        rospy.loginfo(msg)
        rate.sleep()

if __name__ == "__main__" :
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
    