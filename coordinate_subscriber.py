#!/usr/bin/env python
import rospy
from assignment.msg import coordinate


def callback(msg):
    print(int(msg.x[0]))
   
    print(int(msg.x[1]))
    
    print(int(msg.x[2]))
    
rospy.init_node("coordinate_subscriber", anonymous=True)
rospy.Subscriber("centers", coordinate, callback)
rospy.spin()




    
