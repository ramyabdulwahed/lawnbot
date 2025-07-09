# ROS2 and GPIO control libraries
import rclpy
from rclpy.node import Node
import lgpio  # Library to control GPIO pins on Raspberry Pi

# ROS2 service and message types
from std_srvs.srv import Trigger
from std_msgs.msg import String
from std_msgs.msg import Bool


PUMP_GPIO = 16        # The physical GPIO pin connected to the pump
GPIO_NUMBER = 4       # Refers to /dev/gpiochip4 (hardware GPIO controller)
ON = 1                # High signal = pump ON
OFF = 0               # Low signal = pump OFF
TIMER_PERIOD = 0.5    # How long to keep the pump ON before turning it OFF (in seconds)



#####gpio setup ########
def open_gpio():
    """Set up the GPIO connection to control the pump."""
    h = lgpio.gpiochip_open(GPIO_NUMBER)  # Open access to the GPIO chip
    return h  # Handle used to control pins

######## Main Pump Controller Node #######################

class PumpController(Node):
    def __init__(self):
        super().__init__('pump_controller')  # Create the ROS2 node

        #This creates the /pump_trigger_service, which main_logic_controller.py calls when it wants to spray.
        self.srv = self.create_service(
            Trigger,
            'pump_trigger_service',
            self.pump_trigger_callback
        )
        self.get_logger().info('Pump Trigger service server is ready')

        self.pump_shutoff_timer = self.create_timer(
            TIMER_PERIOD,                    # 0.5 seconds
            self.timer_callback,             # Function to call
            autostart=False                  # Don’t run it right away
        )
        self.pause_pub = self.create_publisher(Bool, '/pause_cmd_vel', 10)

        #This opens GPIO access so we can control the pump relay through code.
        self.h = open_gpio()


    ################ Service Callback: When /pump_trigger_service is called ################################
    def pump_trigger_callback(self, request, response):

        self.pause_pub.publish(Bool(data=True)) # Pause any ongoing movement commands

        self.get_logger().info('Trigger service called')
        
        self.turn_on_pump()           # Turn on the pump
        self.pump_shutoff_timer.reset()  # Start the timer to turn it off after 0.5s
        
        response.success = True
        response.message = f"Action triggered successfully: Pump Triggered"
        return response


    ######################## Turn Pump ON / OFF  #####################
    def turn_on_pump(self):
        lgpio.gpio_write(self.h, PUMP_GPIO, ON)
        self.get_logger().info('Pump turned ON')
        
    def turn_off_pump(self):
        lgpio.gpio_write(self.h, PUMP_GPIO, OFF)
        self.get_logger().info('Pump turned OFF')


    ################ timer callback ####################333
    def timer_callback(self):
        """Called automatically after 0.5s to shut the pump off."""
        self.get_logger().info('Timer triggered - turning off pump')
        self.turn_off_pump()
        self.pump_shutoff_timer.cancel()  # Stop the timer

        #here
        self.pause_pub.publish(Bool(data=False))  # Resume movement commands
    ###################### clean gpio ################
    def close_gpio(self):
        """Clean up GPIO when shutting down."""
        self.turn_off_pump()
        lgpio.gpiochip_close(self.h)




def main(args=None):
    rclpy.init(args=args)
    pump_controller = PumpController()

    try:
        rclpy.spin(pump_controller)  # Run the node
    except KeyboardInterrupt:
        pump_controller.get_logger().info("Caught Ctrl+C, shutting down pump controller.")
        pump_controller.close_gpio()
    finally:
        rclpy.shutdown()

if __name__ == '__main__':
    main()
