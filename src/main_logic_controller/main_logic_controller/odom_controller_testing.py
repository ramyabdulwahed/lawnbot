import rclpy
from rclpy.node import Node
import math
from geometry_msgs.msg import TransformStamped, Quaternion
from tf2_ros import TransformBroadcaster
from nav_msgs.msg import Odometry

import tf_transformations


class MotorController(Node):
    def __init__(self):
        super().__init__('motor_controller_node')

        # Publisher
        self.odom_pub = self.create_publisher(Odometry, '/odom', 10)

        # TF broadcaster
        self.tf_broadcaster = TransformBroadcaster(self)

        # Robot pose state
        self.x = 0.0
        self.y = 0.0
        self.theta = 0.0

        # Simulated encoder state (for test mode)
        self.ticks_drive = 0
        self.ticks_turn = 0
        self.last_ticks_drive = 0
        self.last_ticks_turn = 0

        # Robot parameters
        self.ticks_per_meter = 5000
        self.ticks_per_radian = 1178

        # Timer (example: 20Hz → every 0.05 seconds)
        self.create_timer(0.05, self.odom_update_callback)

    def odom_update_callback(self):
        # === SIMULATE ENCODER DATA ===
        # Pretend robot is moving forward and turning slowly:
        self.ticks_drive += 50      # +50 ticks per loop → forward
        self.ticks_turn += 5        # +5 ticks per loop → rotating slowly

        # === Compute deltas ===
        delta_ticks_drive = self.ticks_drive - self.last_ticks_drive
        delta_ticks_turn = self.ticks_turn - self.last_ticks_turn

        delta_distance = delta_ticks_drive / self.ticks_per_meter
        delta_theta = delta_ticks_turn / self.ticks_per_radian

        # === Update heading (theta) ===
        self.theta += delta_theta
        self.theta = (self.theta + math.pi) % (2 * math.pi) - math.pi  # normalize

        # === Update X and Y ===
        self.x += delta_distance * math.cos(self.theta)
        self.y += delta_distance * math.sin(self.theta)

        # === Save last ticks ===
        self.last_ticks_drive = self.ticks_drive
        self.last_ticks_turn = self.ticks_turn

        # === Publish Odometry ===
        odom_msg = Odometry()
        odom_msg.header.stamp = self.get_clock().now().to_msg()
        odom_msg.header.frame_id = 'odom'
        odom_msg.child_frame_id = 'base_link'

        odom_msg.pose.pose.position.x = self.x
        odom_msg.pose.pose.position.y = self.y
        odom_msg.pose.pose.position.z = 0.0

        q = tf_transformations.quaternion_from_euler(0, 0, self.theta)
        odom_msg.pose.pose.orientation = Quaternion(x=q[0], y=q[1], z=q[2], w=q[3])

        self.odom_pub.publish(odom_msg)

        # === Publish TF ===
        t = TransformStamped()
        t.header.stamp = self.get_clock().now().to_msg()
        t.header.frame_id = 'odom'
        t.child_frame_id = 'base_link'

        t.transform.translation.x = self.x
        t.transform.translation.y = self.y
        t.transform.translation.z = 0.0

        t_q = tf_transformations.quaternion_from_euler(0, 0, self.theta)
        t.transform.rotation.x = t_q[0]
        t.transform.rotation.y = t_q[1]
        t.transform.rotation.z = t_q[2]
        t.transform.rotation.w = t_q[3]

        self.tf_broadcaster.sendTransform(t)



def main():
    rclpy.init(args=None)
    node = MotorController()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
if __name__ == '__main__':
    main()