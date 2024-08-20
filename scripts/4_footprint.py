#! /usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from geometry_msgs.msg import PoseStamped, PoseWithCovarianceStamped, Twist
from std_msgs.msg import Float32
import math

class Log_Position():
    def __init__(self):
        rospy.init_node('tag_position', anonymous=True)

        ### sub ###
        rospy.Subscriber('/amcl_pose', PoseWithCovarianceStamped, self.amcl_pose_callback)

    def amcl_pose_callback(self, data):

        self.P_x = data.pose.pose.position.x
        self.P_y = data.pose.pose.position.y
        self.P_z = data.pose.pose.position.z
    
        self.O_x = data.pose.pose.orientation.x
        self.O_y = data.pose.pose.orientation.y
        self.O_z = data.pose.pose.orientation.z
        self.O_w = data.pose.pose.orientation.w

        self.print_position()

    def print_position(self):
        print("position: ({:.2f}, {:.2f}, {:.2f})".format(self.P_x,self.P_y,self.P_z))
        print("orientation: ({:.2f}, {:.2f}, {:.2f}, {:.2f})".format(self.O_x,self.O_y,self.O_z,self.O_w))

    def run(self):
        rospy.spin()

if __name__ == '__main__':
    try:
        log_position = Log_Position()
        log_position.run()
    except rospy.ROSInterruptException:
        pass
