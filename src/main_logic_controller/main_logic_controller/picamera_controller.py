import cv2
import rclpy
from picamera2 import Picamera2
import numpy as np
from time import sleep

from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

from rclpy.node import Node

from std_msgs.msg import String
from std_srvs.srv import Trigger

FRAME_CAPTURE_RATE = 0.05  # time between each frame capture in seconds (20 fps means that we take a picture every 0.05 seconds)
############################# big picture #############################
#Waits for an external model (via ROS service) to be "ready" 
# Captures camera frames using PiCamera2 every 0.05s (20 fps) 
# Converts the images to ROS format 
# Publishes them to a topic called 'image' for other nodes (e.g., object detection) to use
####################### side note #######################
#Latency = the delay between event happening and data being received.
#low latency = low delay. 
#rclpy.qos.qos_profile_sensor_data - means - Qos means quality of service. 
# qos_profile_sensor_data is a preset designed for: Low latency. 
# meaning This profile is designed for real-time sensor feeds like cameras and LIDAR, where latest data is more important than old data.
#####################33
# A frame = one snapshot (image) at a point in time.
# ex. 30 fps means 30 frames per second.





class PiCameraController(Node):

    def __init__(self):
        super().__init__('picamera_controller')  
        # Initialize the node with the name 'picamera_controller'.
        
        self.publisher_ = self.create_publisher(Image, 'image', rclpy.qos.qos_profile_sensor_data)
        # Create a publisher to publish images on the 'image' topic using the Image message type.
        # The QoS profile is set for sensor data to handle high-frequency messages.

        self.picam2 = setup_camera()
        # Call the `setup_camera` function to initialize and configure the Raspberry Pi camera.

        self.bridge = CvBridge() # Create an instance of CvBridge to convert between OpenCV images and ROS Image messages.

        # Wait for the 'model_ready' service to be available before proceeding.
        self.cli = self.create_client(Trigger, 'model_ready')
        # Create a client to call the 'model_ready' service, which checks if the model is ready.

        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info("Model service not available, waiting...")
            # Log a message every second until the 'model_ready' service becomes available.

        self.check_model_status()# Call the `check_model_status` method to ensure the model is ready before starting the camera.

        self.timer = self.create_timer(FRAME_CAPTURE_RATE, self.timer_callback)
        # Create a timer to call the `timer_callback` method at a fixed interval (e.g., 20 times per second).

    def setup_camera(self):
        """Set up the camera to publish images for the model"""
        
        # Create an instance of the Picamera2 class to interact with the camera
        picam2 = Picamera2()
        
        # Create a configuration for still images with the main stream format set to RGB888
        # RGB888 means each pixel is represented by 8 bits for Red, Green, and Blue channels
        config = picam2.create_still_configuration(main={"format": "RGB888"})
        
        # Apply the configuration to the camera
        picam2.configure(config)
        
        # Start the camera to begin capturing images
        picam2.start()
        
        # Pause for 1 second to allow the camera to warm up and stabilize
        sleep(1)
        
        # Access the camera's controls to adjust settings
        with picam2.controls as ctrl:
            
            # Set the exposure time to 5000 microseconds (5 milliseconds)
            #this refers to the duration the camera's sensor is exposed to light when capturing an image. 
            # It's a critical parameter that affects the brightness and clarity of the captured image.
            ctrl.ExposureTime = 5000

        return picam2



    def check_model_status(self):
        req = Trigger.Request()
        while rclpy.ok():
            future = self.cli.call_async(req)
            rclpy.spin_until_future_complete(self, future)
            if future.result().success:
                self.get_logger().info("Model is ready. Proceeding with picamera node execution.")
                break
            self.get_logger().info("Model not ready, retrying...")

    def timer_callback(self):
        frame = self.picam2.capture_array()# Capture an image from the camera as a NumPy array.

        frame = cv2.resize(frame, (1280, 720))
        # Resize the image to 1280x720 resolution to reduce bandwidth usage.

        ros_image = self.bridge.cv2_to_imgmsg(frame, encoding='rgb8')
        # Convert the OpenCV image (NumPy array) to a ROS Image message with 'rgb8' encoding.

        self.publisher_.publish(ros_image)
        # Publish the ROS Image message on the 'image' topic.

        self.get_logger().debug('Taking Picture from PiCamera and Publishing')
        # Log a debug message indicating that an image was captured and published.
            
    def shutdown_camera(self):
        """Shutdown the camera"""
        self.picam2.close()
        print("Camera shutdown")









def main(args=None):
    rclpy.init(args=args)

    picamera_controller = PiCameraController()

    rclpy.spin(picamera_controller)
    picamera_controller.shutdown_camera()
    rclpy.shutdown()


if __name__ == '__main__':
    main()