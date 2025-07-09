#####################side notes##############################
#Serial communication is a way for two devices (e.g., a Raspberry Pi and a motor controller) to talk to each other by sending one piece of data at a time over a wire.
#  in python we use the serial lib to open that channel and send strings

############################# big picture tracing for the program #########################################
# 1. main_logic controller subscribes to /path (for movement path commands) 
# 2. main_logic_controller receives a path message: ex. MotorData(op_code='D', position=1000, speed=300) 
# 3. it publishes it to: Topic: /motor_output Message Type: MotorData 
# 4. motor controller is subsribed to it thus it revices the message and triggers motor_output_callback() which formats the command and sends it over to kangaroo 
# 5. after sending we can start the timer service /motor_start  which repeadelty calls get_completion_status() every 0.1s, 
#  until we get p we publish done to /motion_completed. 




import rclpy                     # ROS 2 client library for Python
from rclpy.node import Node      # Base class for ROS 2 nodes
import serial                    # For serial communication with Kangaroo controller
import time                      # Used for delays and timing

# Standard ROS 2 service and message types
from std_srvs.srv import Empty
from std_msgs.msg import Bool

# Custom message type for motor commands
from main_logic_controller.msg import MotorData

#for the odom and tf stuff
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Quaternion
from tf2_ros import TransformBroadcaster
from geometry_msgs.msg import TransformStamped
import math  
import tf_transformations


################################## kangaroo constants #################################################

# These are Kangaroo serial commands to get position status for each motor
GETPOS_COMMAND_DRIVE = "D,getp"
GETPOS_COMMAND_TURN  = "T,getp"

# Frequency at which we check motor status (every 0.1 seconds)
GET_COMPLETED_ACTION_TIMER_PERIOD = 0.1
ODOM_TIMER_PERIOD = 0.05  # 20 Hz → smooth updates


################################## serial communication function ##################################333


def send_command(ser, command):
    """
    Sends a command to the Kangaroo motion controller via serial
    - Adds carriage return '\r' (required by Kangaroo)
    - Waits briefly and reads back the response
    """
    ser.write(command.encode('utf-8') + b'\r\n')
    time.sleep(0.1) #give kangaroo some time to process the command and respond
    response = ser.read(ser.in_waiting).decode('utf-8') #reads whatever bytes are currently waiting in the serial buffer. decode it into a string
    #ser.in_waiting tells us how many bytes are there in the buffer. ex.mailbox
    return response


def setup_serial():
    """
    Opens a serial connection to Kangaroo and sends startup commands
    - Commands like D,start and T,start initialize the Drive and Turn channels
    - p0 sets the position to 0
    """
    ser = serial.Serial('/dev/ttyAMA0', 9600, timeout=1) #open the serial conneciton by creating a Serial object
    time.sleep(2)  # Let the connection stabilize

    print("Connected to Kangaroo on /dev/ttyAMA0")

    #Initialization commands
    start_commands = ["D,start", "T,start", "D,p0", "T,p0"] #these say in order: 1. start drive channel, start the turn channel, reset drive position to 0, reset turn position to 0.
    for command in start_commands:
        response = send_command(ser, command) #we are sending the commands one by one and reading back the response
        print(f"Response for '{command}': {response}")
    
    return ser





######################################33 main class ################################################
class MotorController(Node):
    def __init__(self):
        super().__init__('motor_controller')

        self.subscription = self.create_subscription(
        MotorData,
        'motor_output',               # Listens to motor commands here
        self.motor_output_callback,   # Handles the message
        10
        )

        self.ser = setup_serial()  # Connect to the Kangaroo via UART
        self.motion_complete_publisher_ = self.create_publisher(
            Bool,
            'motion_completed',   # Lets other nodes know when motion is done
            10
        )
        self.odom_pub = self.create_publisher(Odometry, '/odom', 10)
        self.tf_broadcaster = TransformBroadcaster(self) #this will be used to broadcast the odometry transform 

        #i commented this out because it is not used with nav2

        # self.timer = self.create_timer(
        #     GET_COMPLETED_ACTION_TIMER_PERIOD,              # every 0.1 seconds
        #     self.publish_completion_status_timer_callback,  # run this function
        #     autostart=False                                 # don't start it yet
        # )

        #this timer we call every 0.05 seconds to update the odometry
        self.odom_timer = self.create_timer(
            ODOM_TIMER_PERIOD, 
            self.odom_update_callback)


        #create  services to start/stop motor
        self.create_service(Empty, 'motor_start', self.start_motor_callback)
        self.create_service(Empty, 'motor_stop',  self.stop_motor_callback)

        #some vairables we will need for odometry
        self.x = 0.0
        self.y = 0.0
        self.theta = 0.0
        self.last_ticks_drive = 0
        self.last_ticks_turn = 0

    #check if motion is complete - will be called by the function below

    #i commented this out because it is not used with nav2

    # def get_completion_status(self):
    #     """
    #     Ask Kangaroo if both DRIVE (D) and TURN (T) motors are done moving.
    #     - Kangaroo replies with 'P=...' once position is reached
    #     - We return True if both report 'P'
    #     -Kangaroo will reply with something like: D,P=1000: this means position has been reached
    #     - So the code checks if both responses contain 'P' (position reached flag). 
    #     -This lets the robot know: I finished moving"
        
        
    #     """
    #     #a capital P in the response means position has been reached a lowercase p means it is still moving
    #     response_drive = send_command(self.ser, GETPOS_COMMAND_DRIVE)
    #     response_turn  = send_command(self.ser, GETPOS_COMMAND_TURN)
    #     return 'P' in response_drive and 'P' in response_turn




    #timer callback function - 
    #i commented this out because it is not used with nav2

    # def publish_completion_status_timer_callback(self):
    #     msg = Bool()
    #     msg.data = self.get_completion_status()  # True = motion done
    #     self.motion_complete_publisher_.publish(msg)
    #     self.get_logger().debug('Publishing motion status: "%s"' % str(msg.data))


    #Listens to movement commands from the logic node and sends them to Kangaroo.

    def motor_output_callback(self, msg):
        """
        Called when a MotorData message arrives.
        - Format: <op_code>,PI<position>S<speed>
        - op_code: 'D' for drive, 'T' for turn
        - PI: the motor will go specific position relative to its current position
        - S: speed
        Example: D,PI1000S200
        """
        #formatting and checking the message
        #command = f'{msg.op_code},pi{msg.position}s{msg.speed}'
        command = f'{msg.op_code},s{msg.speed}'
        self.get_logger().info(f'Sending to Serial: {command}')

        response = send_command(self.ser, command)
        #print(f"Response: {response}")
        print ("response sent!")

    def stop(self):
        """
        Sends commands to stop both motors
        """
        send_command(self.ser, "D,s0")
        send_command(self.ser, "T,s0")
        self.get_logger().info('Stopping motors')


    def stop_and_shutdown(self):
        self.stop()
        self.ser.close()
        self.get_logger().info('Stopped and closed serial connection')


    def stop_motor_callback(self, request, response):
        self.stop()
        self.timer.cancel()  # Stop checking for completion
        self.motion_complete_publisher_.publish(Bool(data=False))  # Notify that it's not moving
        return Empty.Response()
    
    def start_motor_callback(self, request, response):
        self.timer.reset()  # Start/resume completion checker
        return Empty.Response()
    


    def odom_update_callback(self):
        """
        This function runs every 0.05 seconds.

        PURPOSE:
        - Query Kangaroo: "Where is the robot now?"
        - Convert encoder ticks → meters (forward position), radians (rotation)
        - Publish /odom → so ROS knows where the robot is
        - Publish TF → so Nav2 / RViz / SLAM can visualize robot pose
        """
        response_drive = send_command(self.ser, "D,getp")

        if response_drive.startswith('D,'):
            response = response_drive.split(',')
            ticks_drive = response[1]
            ticks_drive = int(ticks_drive[1:])  # Remove 'p' and convert to int
        else:
            self.get_logger().warn(f"Unexpected Drive reply: {response_drive}")
            return 
        


        # === STEP 2 — Query TURN axis encoder ===
        # Example expected reply: T=5678 → means turn encoder = 5678 ticks

        response_turn = send_command(self.ser, "T,getp")
        
        if response_turn.startswith('T,'):
            response = response_turn.split(',')
            ticks_turn = response[1]
            ticks_turn = int(ticks_turn[1:])
        else:
            self.get_logger().warn(f"Unexpected Turn reply: {response_turn}")
            return  
        
          # === STEP 3 — Convert TICKS → meters and radians ===

        ticks_per_meter = 5000 
        ticks_per_radian = 1178 

        # Now we convert:
        delta_ticks_drive = ticks_drive - self.last_ticks_drive
        delta_ticks_turn = ticks_turn - self.last_ticks_turn

        delta_distance = delta_ticks_drive / ticks_per_meter  # meters moved forward
        delta_theta = delta_ticks_turn / ticks_per_radian    # radians turned

        # Update last ticks for next iteration
        self.last_ticks_drive = ticks_drive
        self.last_ticks_turn = ticks_turn

        self.theta += delta_theta  # Update orientation meaning we are adding the change in angle to the previous angle
        #normalize theta to be between -pi and pi
        self.theta = (self.theta + math.pi) % (2 * math.pi) - math.pi

        self.x += delta_distance * math.cos(self.theta)  # Update x position
        self.y += delta_distance * math.sin(self.theta)


        # === STEP 4 — Publish Odometry message ==
        #"I am publishing the pose of base_link relative to odom frame."
        odom_msg = Odometry()
        odom_msg.header.stamp = self.get_clock().now().to_msg() #when this odom was computed
        odom_msg.header.frame_id = 'odom'        # Frame "odom" is the world frame
        odom_msg.child_frame_id = 'base_link'    # Robot's base frame

        #a pose contains position and orientation
        #point position #x y z
        #quaternion orientation #x y z w
        odom_msg.pose.pose.position.x = self.x
        odom_msg.pose.pose.position.y = self.y
        odom_msg.pose.pose.position.z = 0.0
        # Convert theta to quaternion for ROS
        #quaternion is a way to represent orientation in 3D space
        #in our case we are using a 2D robot so we only need to represent rotation around the z-axis, the x and y components will be 0
        q = tf_transformations.quaternion_from_euler(0, 0, self.theta)
        odom_msg.pose.pose.orientation = Quaternion(x=q[0], y=q[1], z=q[2], w=q[3])

        # Set the twist (velocity) of the robot
        odom_msg.twist.twist.linear.x = delta_distance / ODOM_TIMER_PERIOD
        odom_msg.twist.twist.angular.z = delta_theta / ODOM_TIMER_PERIOD

        self.odom_pub.publish(odom_msg)

        # === STEP 5 — Publish TF transform ===
        t = TransformStamped() #ros2 message type for broadcasting frame relationships

        #the below is saying: At this time, base_link exists relative to odom at the pose we are about to set.
        t.header.stamp = self.get_clock().now().to_msg()
        t.header.frame_id = 'odom'
        t.child_frame_id = 'base_link'

        t.transform.translation.x = self.x
        t.transform.translation.y = self.y
        t.transform.translation.z = 0.0
        
        q = tf_transformations.quaternion_from_euler(0,0,self.theta)
        t.transform.rotation.x = q[0]
        t.transform.rotation.y = q[1]
        t.transform.rotation.z = q[2]
        t.transform.rotation.w = q[3]

        self.tf_broadcaster.sendTransform(t)






def main(args=None):
    rclpy.init(args=args)
    motor_controller = MotorController()

    try:
        rclpy.spin(motor_controller)  # Keep it running
    except KeyboardInterrupt:
        motor_controller.get_logger().info("Caught Ctrl+C, shutting down...")
        motor_controller.stop_and_shutdown()
    finally:
        rclpy.shutdown()

if __name__ == '__main__':
    main()





