import rclpy
from rclpy.node import Node
from nav_msgs.msg import Odometry

'''
about this node:
This node bridges the /diff_cont/odom topic to the /odom topic.
It is used to ensure that the odometry data from the differential drive controller is available on the standard /odom topic for slam and other navigation purposes.
'''

class OdomBridge(Node):
    def __init__(self):
        super().__init__('odom_bridge')
        self.sub = self.create_subscription(Odometry, '/diff_cont/odom', self.callback, 10)
        self.pub = self.create_publisher(Odometry, '/odom', 10)

    def callback(self, msg):
        self.pub.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = OdomBridge()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
