# ROS 2 Python interface
import rclpy
from rclpy.node import Node

# Standard ROS message types
from std_msgs.msg import String
from std_srvs.srv import Trigger, Empty

# Custom message types for this project
from main_controller_interfaces.msg import MotorData, BoundingBox

# Constants to define spray zone area (Y-axis center of the image)
Y_MIDPOINT = 500        # Vertical midpoint of the camera image
Y_RANGE = 50            # Acceptable margin around the midpoint for spraying


class MainLogicController(Node):
    def __init__(self):
        super().__init__('main_logic_controller')  # Create the node with a name


         # Subscribe to 'path' topic to get movement instructions
        self.path_subscription = self.create_subscription(
            MotorData,              # Custom message with movement commands
            'path',                 # Topic name
            self.path_callback,     # What to do when a message arrives
            10                      # Queue size (how many messages to buffer)
        )

        # Subscribe to 'bound_box' topic to get bounding box data from object detection
        # self.bound_box_subscription = self.create_subscription(
        #     BoundingBox,                 # Custom message for detected object
        #     'bound_box',                 # Topic name
        #     self.dandelion_detected_callback,  # Called when object detected
        #     10
        # )

        # Store the current movement command (so we know if we're moving forward)
        self.current_path = MotorData(op_code='D', position=0, speed=0)

        # Boolean flag to control whether spraying is enabled
        self.run_pump = False

        # Define two service servers: to start and stop the pump logic
        #the callbacks are called whenever the service is called immeditaley to do the action. and the name of the service is the 2nd arg
        self.create_service(Empty, 'pump_start', self.start_pump_callback)
        self.create_service(Empty, 'pump_stop', self.stop_pump_callback)

        # Create a service client to control the pump
        self.pump_client = self.create_client(Trigger, 'pump_trigger_service')
        while not self.pump_client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('pump service not available, waiting again...')

        # Create a service client to control lights
        self.light_client = self.create_client(Trigger, 'light_trigger_service')
        while not self.light_client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('light service not available, waiting again...')

        # Publisher that sends commands to the motor controller node
        self.motor_output_publisher_ = self.create_publisher(MotorData, 'motor_output', 10)
        self.setup()  # Call the setup method to turn on the light at startup


###################### light setp and control ##################################################
    def setup(self):
        self.send_light_request()  # Turn on the light when robot starts

    def send_light_request(self):
        request = Trigger.Request()
        future = self.light_client.call_async(request)
        future.add_done_callback(self.light_callback) #avfter we get a response we call the light_callback function below.

    def light_callback(self, future):
        response = future.result()
        if response.success:
            self.get_logger().debug(f'Light Service response: {response.message}')
        else:
            self.get_logger().debug('Light Service call failed')



########################### pump ############################################

    def send_pump_request(self):
        request = Trigger.Request()
        future = self.pump_client.call_async(request)
        future.add_done_callback(self.pump_callback)

    def pump_callback(self, future):
        response = future.result()
        if response.success:
            self.get_logger().info(f'Pump Service response: {response.message}')
        else:
            self.get_logger().info('Pump Service call failed')


#############################3 movement - takes care of path publishing #############################3
    def path_callback(self, msg):
        # When new path data is received, forward it to the motor
        self.motor_controller_callback(msg)

    def motor_controller_callback(self, msg):
        self.current_path = msg  # Save the latest movement instruction
        self.motor_output_publisher_.publish(msg)  # Send it to the motor node
        self.get_logger().info(f'Publishing: "{msg}"')

######################### dandelions ##############################33
    def dandelion_detected_callback(self, msg):
        # Called when a dandelion is detected

        #Only spray if the weed is vertically centered in the image — i.e., right in front of the nozzle

        y_midpoint = msg.center_y  # Vertical center of bounding box
        in_range = (Y_MIDPOINT - Y_RANGE) <= y_midpoint <= (Y_MIDPOINT + Y_RANGE)

        if in_range:
            self.get_logger().info(f'Dandelion is within range at: {y_midpoint}')
            # Check if robot is moving forward AND pump is enabled
            if 'D' in self.current_path.op_code and self.run_pump:
                self.send_pump_request()

    def start_pump_callback(self, request, response):
        self.run_pump = True  # Enable spraying 
        return Empty.Response()

    def stop_pump_callback(self, request, response):
        self.run_pump = False  # Disable spraying
        return Empty.Response()




def main(args=None):
    rclpy.init(args=args)
    node = MainLogicController ()
    rclpy.spin (node)
    rclpy.shutdown()
