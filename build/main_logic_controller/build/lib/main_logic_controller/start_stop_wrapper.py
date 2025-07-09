##################3  big pciture ##########################



import rclpy 
from rclpy.node import Node
from std_srvs.srv import SetBool, Empty

class WrapperNode(Node):
    def __init__(self):
        super().__init__('start_stop_wrapper')

        #creating a service: that takes true, false. True = start everything, False = stop everything.
        self.srv = self.create_service(SetBool, 'wrapper_service', self.wrapper_callback)

        #creating clients for each of the services that we want to start/stop.
        self.motor_start = self.create_client(Empty, 'motor_start')
        self.motor_stop = self.create_client(Empty, 'motor_stop')
        self.path_start = self.create_client(Empty, 'path_start')
        self.path_stop = self.create_client(Empty, 'path_stop')
        self.pump_start = self.create_client(Empty, 'pump_start')
        self.pump_stop = self.create_client(Empty, 'pump_stop')

    #callback function that gets called when the service is called. it takes in a request which is a boolean (true or false).
    def wrapper_callback(self, request, response):
        command = request.data  # True = start, False = stop
        action = "starting" if command else "stopping"
        self.get_logger().info(f"Received request: {action} services.")

        #based on the command, we call the appropriate service.
        if command:
            #trigger_service is a function that takes in a service client and calls it.
            #self.trigger_service(self.motor_start, self.path_start, self.pump_start)
            self.trigger_service(self.motor_start)
        else:
            #self.trigger_service(self.motor_stop, self.path_stop, self.pump_stop)
            self.trigger_service(self.motor_stop)
        #respond to the service request
        response.success = True
        response.message = f"Sent {action} command."
        return response


def main(args=None):
    rclpy.init(args=args)
    node = WrapperNode()
    rclpy.spin(node)
    rclpy.shutdown()
if __name__ == '__main__':
    main()
