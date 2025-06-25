import rclpy
from rclpy.node import Node
from std_msgs.msg import Bool
import os

class ExplorationMonitor(Node):
    def __init__(self):
        super().__init__('exploration_monitor')

        self.create_subscription(Bool, '/exploration_done', self.done_callback, 10)
        self.get_logger().info("Exploration Monitor started...")

    def done_callback(self, msg):
        if msg.data:
            self.get_logger().info("Exploration complete! Saving map and starting Nav2...")
        
            # Save map (call service)
            os.system("ros2 service call /slam_toolbox/save_map slam_toolbox/srv/SaveMap \"{name: 'bestmap1000', directory: '/home/ramy_abdulwahed/41xx/src/main_logic_controller/config'}\"")
            
            # # Optional: kill SLAM Toolbox (needs care!)
            # os.system("pkill slam_toolbox")

            # os.system("ros2 launch nav2_bringup localization_launch.py map:=bestmap.yaml use_sim_time:=true")
            
            # # Start Nav2 (simple example)
            # os.system("ros2 launch nav2_bringup navigation_launch.py map:=bestmap.yaml use_sim_time:=true map_subscribe_transient_local:=true")
