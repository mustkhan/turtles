#!/usr/bin/env python3
import rospy
import math
from geometry_msgs.msg import Twist
from std_msgs.msg import String

def publisher_node():
    """Initialize publisher node and 
    publish wheel command to the cmd_vel topic')"""
    rospy.init_node("motor")
    cmd_pub = rospy.Publisher('cmd_vel', Twist, queue_size=1)
    rate = rospy.Rate(10)
    
    twist = Twist()

    # NOTE: Lab 1 asks us to command the wheel to go 
    # forward 1 m, rotate 360◦, and then stop.
    
    # Move forward for 4.5 seconds (1 m)
    twist.linear.x = 0.26
    twist.angular.z = 0
    start = rospy.get_rostime().to_sec()
    while not rospy.is_shutdown() and rospy.get_rostime().to_sec() - start < 4.5:
        cmd_pub.publish(twist)
        rate.sleep()
    
    # Rotate in place for 6 seconds (360◦ rotation)
    twist.linear.x = 0
    twist.angular.z = 1
    start = rospy.get_rostime().to_sec()
    while not rospy.is_shutdown() and rospy.get_rostime().to_sec() - start < 6:
        cmd_pub.publish(twist)
        rate.sleep()
    
    # Stop motion
    twist.linear.x = 0
    twist.angular.z = 0
    cmd_pub.publish(twist)

def main():
    try:
        rospy.init_node('motor')
        publisher_node()
    except rospy.ROSInterruptException:
        pass


if __name__ == "__main__":
    main()
