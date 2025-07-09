import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import time

class OdometryTester(Node):
    def __init__(self):
        super().__init__('odometry_tester')
        self.publisher_ = self.create_publisher(Twist, '/cmd_vel', 10)
        self.timer_ = self.create_timer(0.1, self.timer_callback)
        self.test_phase = 'forward'
        #         self.get_clock().now()  ->Returns the current ROS 2 time, as a special time object
        # .seconds_nanoseconds()  -> Converts it to a tuple ex. (seconds, nanoseconds)
        # .seconds_nanoseconds()[0] ->Just means: "give me the seconds only"

        self.start_time = self.get_clock().now().seconds_nanoseconds()[0] 
        self.sent_stop = False

    def timer_callback(self):
        current_time = self.get_clock().now().seconds_nanoseconds()[0]
        msg = Twist()

        if self.test_phase == 'forward':
            if current_time - self.start_time < 20:  # Move forward for 5 seconds
                msg.linear.x = 0.05  # m/s
                self.publisher_.publish(msg)
            else:
                msg.linear.x = 0.0
                self.publisher_.publish(msg)
                self.test_phase = 'done'
                self.get_logger().info("✅ Done. The robot should have moved ~1 meter forward.")
                self.get_logger().info("📍 Now check RViz2: does /odom show ~1m forward movement?")
        elif self.test_phase == 'done' and not self.sent_stop:
            self.publisher_.publish(Twist())  # Ensure full stop
            self.sent_stop = True


def main(args=None):
    rclpy.init(args=args)
    node = OdometryTester()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
