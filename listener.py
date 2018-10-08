#!/usr/bin/env python


import rospy
from beginner_tutorials.msg import centre

def callback(data):
    rospy.loginfo(data.centre)
    print(data.centre)


def listener():

    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber('centres', centre, callback)

    
    rospy.spin()

if __name__ == '__main__':
    listener()
