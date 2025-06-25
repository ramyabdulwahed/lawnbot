
#todo: go over the rsp.launch.py file and get rid of the if statements 
import os #for file paths
from ament_index_python.packages import get_package_share_directory #find where a ros2 package is installed
from launch import LaunchDescription #building blocks to launch nodes
from launch.actions import IncludeLaunchDescription, ExecuteProcess, TimerAction #to include other launch files or run processes. TimerAction is used to delay the launching of a node
from launch.launch_description_sources import PythonLaunchDescriptionSource #used with IncludeLaunchDescription to specify a Python launch file
from launch.substitutions import Command #runs shell commands and uses the output as a substitution for a param value for ex.
from launch.actions import RegisterEventHandler #to register event handlers that can react to events in the launch system
from launch.event_handlers import OnProcessStart #to trigger actions
from launch_ros.actions import Node #to create ROS 2 nodes in the launch file

def generate_launch_description():

    package_name = 'main_logic_controller'

    rps = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([os.path.join(get_package_share_directory(package_name), 'launch', 'rsp.launch.py')]), 
        launch_arguments={'use_sim_time': 'true', 'use_ros_control':'true'}.items()
    )

    #executing a shell command to get the value of robot description from the ros param server

    robot_description = Command (['ros2 param get --hide-type /robot_state_publisher robot_description'])

    controller_param_file = os.path.join(get_package_share_directory(package_name), 'config', 'my_controllers.yaml')

    #starts the controller manager node, which takes in the robot description and the controller parameters
    controller_manager = Node (
        package = 'controller_manager',
        executable= 'ros2_control_node',
        parameters=[{'robot_description': robot_description}, controller_param_file]
    )

    #wait 3sec before starting the controller manager node
    #this is useful to ensure that the robot description is available before starting the controller manager
    delayed_controller_manager = TimerAction(period=3.0, actions=[controller_manager])

    #spwans the diff drive controller in the yaml file with the name 'diff_cont'
    diff_drive_spawner = Node(
        package='controller_manager', 
        executable='spawner', 
        arguments=['diff_cont'],
        )
    #wait until  controller manager is up before spawning the diff controller
    delayed_diff_drive_spawner = RegisterEventHandler(
        event_handler=OnProcessStart(
            target_action=controller_manager,  # Wait for the controller manager to start
            on_start=[diff_drive_spawner]  # Then spawn the diff drive controller
        )
    )

    joint_broad_spawner = Node (
        package = 'controller_manager',
        executable = 'spawner',
        arguments = ['joint_broad'],
    )

    delayed_diff_drive_spawner = RegisterEventHandler(
        event_handler=OnProcessStart(
            target_action=controller_manager,  # Wait for the controller manager to start
            on_start=[joint_broad_spawner]  # Then spawn the diff drive controller
            )
    )
    

    return LaunchDescription([
        rps,
        delayed_controller_manager,
        delayed_diff_drive_spawner,
        joint_broad_spawner
    ])