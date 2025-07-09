#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist, TwistStamped

class TwistRelay(Node):
    def __init__(self):
        super().__init__("twist_relay")
        self.controller_sub = self.create_subscription(Twist, "cmd_vel_stamped", self.controller_callback, 10)
        self.controller_pub = self.create_publisher(TwistStamped, "cmd_vel", 10)
    
    
    
    #this function will take the Twist message from the controller and publish it as a TwistStamped message
    def controller_callback(self, msg: Twist):

        twist_stamped = TwistStamped()
        twist_stamped.header.stamp = self.get_clock().now().to_msg()
        twist_stamped.twist = msg
        self.controller_pub.publish(twist_stamped)
        self.get_logger().info(f"Published TwistStamped: {twist_stamped}")


def main():
    rclpy.init()
    twist_relay = TwistRelay()
    rclpy.spin(twist_relay)
    twist_relay.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()