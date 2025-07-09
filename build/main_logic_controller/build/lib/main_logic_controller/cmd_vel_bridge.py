# cmd_vel_bridge.py
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

'''
about this node:
This node bridges the cmd_vel topic to the diff_cont/cmd_vel_unstamped topic.
'''

class CmdVelBridge(Node):
    def __init__(self):
        super().__init__('cmd_vel_bridge')
        self.sub = self.create_subscription(Twist, '/cmd_vel', self.callback, 10)
        self.pub = self.create_publisher(Twist, '/diff_cont/cmd_vel_unstamped', 10)

    def callback(self, msg):
        self.pub.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = CmdVelBridge()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
