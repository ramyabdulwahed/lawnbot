#big picture of this code:
# This code listens to velocity commands from Nav2 and translates them into position and speed commands
# for a motor controller (Kangaroo) that requires specific commands to move the robot.
#thus: nav2 -> cmd_vel_emulator -> motor_controller (Kangaroo)

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from main_controller_interfaces.msg import MotorData
from std_msgs.msg import Bool
from std_srvs.srv import Empty  # Import Empty service for stopping the motor


class CmdVelEmulator(Node):
    def __init__(self):
        super().__init__('cmd_vel_emulator')

        # Create a subscriber to listen to Nav2's velocity commands
        self.subscription = self.create_subscription(
            Twist,
            '/cmd_vel',
            self.cmd_vel_callback,
            10
        )

        self.path_publisher = self.create_publisher(MotorData, 'path', 10)


        # Create a publisher to send position + speed commands to your motor controller
        self.motor_pub = self.create_publisher(
            MotorData,
            'motor_output',
            10
        )

        # Create subscriber to pause/resume streaming to motor controller
        self.paused = False
        self.create_subscription(
            Bool,
            '/pause_cmd_vel',
            self.pause_callback,
            10
        )
        # self.create_service(Empty, 'motor_stop',  self.stop_motor_callback)
        self.motor_stop = self.create_client(Empty, 'motor_stop')
        while not self.motor_stop.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Motor stop service not available, waiting again...')


        # Store the most recent velocity command (initially 0)
        self.latest_linear_x = 0.0
        self.latest_angular_z = 0.0

        # Timer to repeat motion every 0.1s (simulating continuous velocity)
        self.timer_period = 0.1  # seconds
        #self.timer = self.create_timer(self.timer_period, self.send_motor_command)

        # Conversion constants (adjust based on your robot’s config!)
        self.ticks_per_meter = 5435 # example: 5000 encoder ticks = 1 meter
        self.ticks_per_radian = 1178  # example: 2000 ticks = 1 radian of rotation
        self.max_speed_ticks = 1000   # max speed in Kangaroo units

        #THESE VALUES ARE TO BE CHANGED
        self.wheel_radius = 0.0508  # example: 10 cm wheel radius
        self.wheel_separation = 0.425 #0.366  # example: 50 cm between wheels
        self.get_logger().info("CmdVel Emulator initialized")
    
    def pause_callback(self, msg):
        self.motor_stop.call_async(Empty.Request())  # Call the service to stop the motor
        self.paused = msg.data
        self.get_logger().info(f'CmdVel paused = {self.paused}')

    
    
    def cmd_vel_callback(self, msg):
        # Save the latest velocity command from Nav2
        self.latest_linear_x = msg.linear.x
        self.latest_angular_z = msg.angular.z
        self.send_motor_command()

    def send_motor_command(self):
        # Only send if there's motion
        """big picture
        This block: Listens to Nav2 saying: “Move forward at this speed” 
        Then translates that into: “Okay Kangaroo, move this distance at this speed”
        """
        if self.paused:
            self.get_logger().debug('Paused: not sending motor commands.')
            return
        
        if abs(self.latest_linear_x) < 0.01 and abs(self.latest_angular_z) < 0.01:
            self.get_logger().debug('No motion detected, not sending motor commands.')
            return


        
        # If there's motion, calculate the speed for each wheel
        # and publish the appropriate commands to the motor controller

        v = self.latest_linear_x  # Linear velocity in m/s
        w = self.latest_angular_z  # Angular velocity in rad/s


        #if both are 0, send stop commands to stop robot
        # if abs(v) < 0.01 and abs(w) < 0.01:
        #     for side in ['1', '2']:
        #         motor_msg = MotorData()
        #         motor_msg.op_code = side
        #         motor_msg.position = 0
        #         motor_msg.speed = 0
        #         self.motor_pub.publish(motor_msg)
        #     return

        v_left = v - (w * self.wheel_separation / 2)  # Left wheel speed
        v_right = v + (w * self.wheel_separation / 2)  # Right wheel speed
####        self.get_logger().debug(f'Linear: {v}, Angular: {w}, Left: {v_left}, Right: {v_right}')

        # Convert linear speeds to ticks
        speed_ticks_left = int(v_left * self.ticks_per_meter)
        speed_ticks_right = int(v_right * self.ticks_per_meter)

        #create motor command for left wheel
        # motor_msg_left = MotorData()
        # motor_msg_left.op_code = '1'
        # motor_msg_left.position = 0
        # motor_msg_left.speed = speed_ticks_left
        #self.path_publisher.publish(motor_msg_left)  # Publish to path topic
        #create motor command for right wheel

        # motor_msg_right = MotorData()
        # motor_msg_right.op_code = '2'
        # motor_msg_right.position = 0
        # motor_msg_right.speed = speed_ticks_right
        # self.motor_pub.publish(motor_msg_right)


        self.motor_pub.publish(MotorData(left_speed=speed_ticks_left, right_speed=speed_ticks_right))  # Publish both speeds in one message
        
        #the below is for the old motorData format
#->        self.motor_pub.publish(MotorData(op_code='1', position=0, speed=speed_ticks_left))  # Example of a second command
#->        self.motor_pub.publish(MotorData(op_code='2', position=0, speed=speed_ticks_right))  # Example of a second command
####        self.get_logger().info (f'cmd vel: linear = {v} and angular = {w}')
####        self.get_logger().info(f'Published Left: {speed_ticks_left}, Right: {speed_ticks_right}')





            
        # if abs(self.latest_linear_x) > 0.01:
        #     # Calculate distance to move in this time slice
        #     distance_m = self.latest_linear_x * self.timer_period  # d=vt   -> meters
        #     position_ticks = int(distance_m * self.ticks_per_meter) #🔹 Converts meters into Kangaroo ticks or units
        #     speed_ticks = int(abs(self.latest_linear_x) * self.max_speed_ticks)

        #     motor_msg = MotorData()
        #     motor_msg.op_code = 'D'
        #     motor_msg.position = position_ticks
        #     motor_msg.speed = speed_ticks

        #     self.motor_pub.publish(motor_msg)
        #     self.get_logger().info(f'Published Drive: pos={position_ticks}, speed={speed_ticks}')

        # if abs(self.latest_angular_z) > 0.01:
        #     # Calculate angular movement in radians
        #     rotation_rad = self.latest_angular_z * self.timer_period
        #     position_ticks = int(rotation_rad * self.ticks_per_radian)
        #     speed_ticks = int(abs(self.latest_angular_z) * self.max_speed_ticks)

        #     motor_msg = MotorData()
        #     motor_msg.op_code = 'T'
        #     motor_msg.position = position_ticks
        #     motor_msg.speed = speed_ticks

        #     self.motor_pub.publish(motor_msg)
        #     self.get_logger().info(f'Published Turn: pos={position_ticks}, speed={speed_ticks}')


def main(args=None):
    rclpy.init(args=args)
    node = CmdVelEmulator()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
