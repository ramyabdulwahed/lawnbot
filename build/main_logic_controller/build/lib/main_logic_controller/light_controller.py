import rclpy                      
import lgpio                      # Library to control GPIO pins on Raspberry Pi
from rclpy.node import Node       # Base class for all ROS2 nodes
from std_srvs.srv import Trigger  # Service type for "do something" actions (no arguments)


#####side note below ####
# light_ gpio = actual gpio pin number we want to control. meaning physcial pin on the rasberry pi. This pin is connected to your light circuit — sending voltage HIGH (1) or LOW (0) turns it on/off.
# GPIO_NUMBER =This is the Linux device number for the GPIO chip, not the pin.
#basically : GPIO number is a Linux device that talks to the GPIO hardware, and I use it to tell the system: 'Hey, I want to send a signal to pin 20.'"

LIGHT_GPIO = 20      # Pin number on GPIO chip to control the light
GPIO_NUMBER = 4      # GPIO chip number (usually corresponds to /dev/gpiochip4)
ON = 1
OFF = 0
TIMER_PERIOD = 0.5 


def open_gpio():
    """Set up the GPIO Connection."""
    h = lgpio.gpiochip_open(GPIO_NUMBER) #Opens a connection to GPIO chip #4.
     #basically a reference or connection to that chip.
    return h

class LightController(Node):

    def __init__(self):
        super().__init__('light_controller')
        #create a service.Trigger has no request data — it's like just do something now
        self.srv = self.create_service(Trigger, 'light_trigger_service', self.trigger_callback)
        self.get_logger().info('Trigger service server is ready')
        self.h = open_gpio() #Initializes the GPIO chip connection when the node starts.

    def trigger_callback(self, request, response):
        """Service callback to trigger the light."""
        
        self.get_logger().info('Light Trigger service called')
        
        ### Logic for triggering GPIO of light
        self.turn_on_light()
        
        #response to the service request
        response.success = True
        response.message = "Light Action triggered successfully"
        return response
    
    def turn_on_light(self):
        """Turn on the light by writing to the GPIO pin."""
        lgpio.gpio_write(self.h, LIGHT_GPIO, ON)
        self.get_logger().info('Light turned ON')
        
    def turn_off_light(self):
        """Turn off the light by writing to the GPIO pin."""
        lgpio.gpio_write(self.h, LIGHT_GPIO, OFF)
        self.get_logger().info('Light turned OFF')
        
    def close_gpio(self):
        """Close the GPIO Connection."""
        self.turn_off_light()
        lgpio.gpiochip_close(self.h)

