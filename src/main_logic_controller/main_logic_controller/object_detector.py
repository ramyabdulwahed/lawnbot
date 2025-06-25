import rclpy                            # ROS2 Python client library
from rclpy.node import Node             # Base class for all ROS2 nodes
from sensor_msgs.msg import Image       # Message type for camera images
from std_srvs.srv import Trigger        # Used for "is the model ready?" checks
from std_msgs.msg import String
from cv_bridge import CvBridge          # Converts ROS Image ↔ OpenCV image
from custom_message.msg import BoundingBox  # Custom msg for bounding box
from ultralytics import YOLO            # The YOLOv11 model
import numpy as np
import time


MODEL_LOCATION = "/home/lawnbot/.../best_320_full_integer_quant_edgetpu.tflite"
MODEL_SIZE = 320  # Image will be resized to 320x320 before prediction

###################################3 object detector class ####################################
class ObjectDetector(Node):
    def __init__(self):
        super().__init__('object_detector')  # Create ROS node

        #subscribe to camera input
        self.subscription = self.create_subscription(
            Image,                   # Type of message (camera image)
            'image',                # Topic name (camera must publish here)
            self.listener_callback, # Callback to run when image is received
            qos_profile=rclpy.qos.qos_profile_sensor_data  # Fast data
        )

        self.bridge = CvBridge() #will be used to convert between ros images and opencv images given to yolo
        #service for model readiness. meaning it lets the other nodes ask if the model is ready to be used
        self.ready = False
        self.service = self.create_service(Trigger, 'model_ready', self.handle_ready_check)

        self.model = YOLO(MODEL_LOCATION, task='detect')
        self.test_readiness()
        self.ready = True

        #create publishers
        self.publisher = self.create_publisher(BoundingBox, 'bound_box', 10) #Publishes detected objects as bounding boxes (center x/y, width, height)
        self.vid_publisher = self.create_publisher(Image, 'image_annotated', 2)

        self.get_logger().info('Object Detector Node Started')


    #Sends a fake image into the model once to confirm it runs without crashing.
    def test_readiness(self):
        while True:
            dummy_image = np.zeros((640, 640, 3))  # Black image, the 3 here means that eahc pixel has 3 values eg. rgb to talk about it
            self.model.predict(dummy_image, imgsz=MODEL_SIZE)
            self.get_logger().info("Model is ready for detection.")
            break

    #callback function for the service - to check if the model is ready.
    def handle_ready_check(self, request, response):
        response.success = self.ready
        response.message = "Model is ready" if self.ready else "Model is not ready yet"
        return response

#This is the function that gets called every time a camera image is received on the 'image' topic.

    def listener_callback(self, msg):
        self.get_logger().debug('Received Image from PiCamera')
        try:
            cv_image = self.bridge.imgmsg_to_cv2(msg, desired_encoding='rgb8')
            results = self.model.predict(cv_image, imgsz=MODEL_SIZE) ##imgsz=MODEL_SIZE means: “Resize the image to 320 × 320 pixels before giving it to the model

            for result in results: #loop through images usually one
                boxes = result.boxes.xywh  # Get boxes in format (x_center, y_center, width, height)
                #Each of those box[...] values is a PyTorch Tensor — like a small array. .item() extracts its value as a plain Python float.
                # Example:
                # box[0] = tensor(210.4)
                # box[0].item() = 210.4  # Plain float
                for box in boxes:
                    bbox = BoundingBox(
                        center_x = box[0].item(),
                        center_y = box[1].item(),
                        width    = box[2].item(),
                        height   = box[3].item()
                    )
                    #This sends the bounding box out to the /bound_box topic —  main_logic_controller.py is subscribed to this
                    # That’s how the detection and spraying connect.
                    self.publisher.publish(bbox)  # Publish each box to /bound_box

                self.vid_publisher.publish(
                    self.bridge.cv2_to_imgmsg(result.plot(), encoding='rgb8')
                )
        except Exception as e:
                self.get_logger().error(f'Failed to predict model: {e}')


def main(args=None):
    rclpy.init(args=args)
    object_detector = ObjectDetector()
    rclpy.spin(object_detector)
    object_detector.destroy_node()
    rclpy.shutdown()








