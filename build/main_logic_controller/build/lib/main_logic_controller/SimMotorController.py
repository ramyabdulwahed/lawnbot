import rclpy
from rclpy.node import Node
from main_controller_interfaces.msg import MotorData
from std_msgs.msg import Float64

class SimMotorController(Node):
    def __init__(self):
        super().__init__('sim_motor_controller')

        self.subscription = self.create_subscription(MotorData, 'motor_output', self.motor_callback, 10)
        self.left_pub = self.create_publisher(Float64, '/left_track_velocity_controller/commands', 10)
        self.right_pub = self.create_publisher(Float64, '/right_track_velocity_controller/commands', 10)

        self.get_logger().info("Simulated motor controller is running.")
    def motor_callback(self, msg):
        speed = float(msg.speed)  # Ensure it's a float
        op = msg.op_code.upper()

        left_cmd = Float64()
        right_cmd = Float64()

        if op == 'D':
            left_cmd.data = speed
            right_cmd.data = speed
        elif op == 'T':
            left_cmd.data = speed
            right_cmd.data = -speed
        else:
            self.get_logger().warn(f"Unknown op_code '{op}', stopping.")
            left_cmd.data = 0.0
            right_cmd.data = 0.0

        # Publish to both controllers
        self.left_pub.publish(left_cmd)
        self.right_pub.publish(right_cmd)

        self.get_logger().info(f"Applied: L={left_cmd.data}, R={right_cmd.data}")


def main(args=None):
    rclpy.init(args=args)
    node = SimMotorController()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info("Shutting down SimMotorController.")
    finally:
        rclpy.shutdown()

