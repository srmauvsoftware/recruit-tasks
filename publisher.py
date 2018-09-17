#!/usr/bin/env python
import rospy
import numpy as np
import cv2
from assignment.msg import coordinate
from auv import coordinatex

e = []
e = coordinatex()
def talker():
    pub = rospy.Publisher("centers", coordinate, queue_size=10)
    rospy.init_node("image", anonymous=True)
    rate = rospy.Rate(10)
    msg = coordinate()
    msg.x = coordinatex()
    
    
    
    
    while not rospy.is_shutdown():
        rospy.loginfo(msg)
        pub.publish(msg)
            
       
        rate.sleep()
if __name__=="__main__":
    try:
        talker()
    except rospy.ROSInterruptException:
        pass

        

