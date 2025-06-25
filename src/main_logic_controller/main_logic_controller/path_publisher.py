import rclpy
from itertools import cycle
from rclpy.node import Node

from std_msgs.msg import String
from std_msgs.msg import Bool
from std_srvs.srv import Trigger, Empty
from main_logic_controller.msg import MotorData


PATH_TIMER_PERIOD = 1 #every 1s that timer will run to check if its allowed to publish the next move command

motor_data_array = [
        MotorData(op_code='D', position=10000, speed=600),
        MotorData(op_code='T', position=1850, speed=500),
        MotorData(op_code='D', position=2200, speed=600),
        MotorData(op_code='T', position=1800, speed=500)
    ]

class PathPublisher(Node):

    def __init__(self):
        super().__init__('path_publisher')
        #Publishes MotorData messages to the topic /path This is what main_logic_controller.py listens to
        self.publisher_ = self.create_publisher(MotorData, 'path', 10)
        
        #This listens to the topic /motion_completed → which is published by motor_controller.py 
        # msg.data = True when the movement is done 
        # msg.data = False while still moving 
        # So we only publish the next move when the robot finishes the previous one.
        self.get_completed_subscription = self.create_subscription(
            Bool,
            'motion_completed',  # Topic name must match the publisher's topic
            self.set_action_completed, #called when we receive a message
            10)
        
        self.iterator = cycle(motor_data_array)#This creates a looping playlist from motor_data_array.

        
        self.get_completed_subscription  # Prevent unused variable warning
        self.action_completed = False #Does not give first instruction until response from motor controller
        
        #Readiness Check: Don’t Move Until Model Is Ready
        self.cli = self.create_client(Trigger, 'model_ready') #Creates a client that will call the service /model_ready — from object_detector.py

        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info("Model service not available, waiting...")
            
        self.check_model_status() #checks if model is ready before moving
        
        self.start_service = self.create_service(Empty, 'path_start', self.start_path_callback)
        self.start_service = self.create_service(Empty, 'path_stop', self.stop_path_callback)
        
        self.timer = self.create_timer(PATH_TIMER_PERIOD, self.timer_callback, autostart=False)
        
    ##checks if model is ready before moving    
    def check_model_status(self):
        req = Trigger.Request() #creating an empty request, meaning this is the type/object that will be passed to the service below
        while rclpy.ok(): #Keep trying every second until we get a yes.
            future = self.cli.call_async(req) #Asks the service /model_ready for a response
            rclpy.spin_until_future_complete(self, future)#Waits until the request completes (i.e., the YOLO node responds)
            if future.result().success:
                self.get_logger().info("Model is ready. Proceeding with path node execution.")
                break
            self.get_logger().info("Model not ready, retrying...")


    #If the previous move is finished, get the next move from the list and publish it. 
    # self.action_completed must be True → comes from motor_controller        
    def timer_callback(self):
        if not self.action_completed:
            return
        
        msg = next(self.iterator)
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % str(msg))
        
    #This is triggered by the /motion_completed topic. When movement finishes, this gets called with msg.data = True.
    def set_action_completed(self, msg):
        self.action_completed = msg.data
        if self.action_completed:
            self.get_logger().debug('Action Completed')
        else:
            self.get_logger().debug('Action Incomplete')
            
            
    def stop_path_callback(self, request, response):
        self.timer.cancel()
        response = Empty.Response()
        return response
        
    def start_path_callback(self,request, response):
        self.iterator = cycle(motor_data_array)
        self.timer.reset()
        response = Empty.Response()
        return response
        
def main(args=None):
    rclpy.init(args=args)

    path_publisher = PathPublisher()

    rclpy.spin(path_publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    path_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()