#!/usr/bin/env python

import rospy
import cv2
import numpy as np
from beginner_tutorials.msg import centre
from imgpr import coordinatex

def talker():
    pub = rospy.Publisher('centres',centre, queue_size = 10)
    rospy.init_node('talker',anonymous=True)
    rate = rospy.Rate(10)
    msg = centre()
    msg.coordinate = coordinatex()

    while not rospy.is_shutdown():
        rospy.loginfo(msg)
        pub.publish(msg)
        rate.sleep()


    


if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass


