from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import IncludeLaunchDescription, ExecuteProcess
from launch.launch_description_sources import PythonLaunchDescriptionSource
import os
from ament_index_python.packages import get_package_share_directory
from launch.substitutions import Command
from launch.substitutions import Command, PathJoinSubstitution
from launch.substitutions import FindExecutable
from launch_ros.substitutions import FindPackageShare
import xacro
from launch.actions import TimerAction

def generate_launch_description():
    pkg_path = get_package_share_directory('main_logic_controller')

        #this will launch rviz2 with a specific configuration file
    rviz_config_file = os.path.join(pkg_path, 'config', '41xxRobotRviz.rviz')
    rviz_node = Node (
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        output='screen',
        arguments=['-d', rviz_config_file],
        parameters=[{'use_sim_time': True}]
    )


    slam_toolbox = get_package_share_directory('slam_toolbox')
    slam_launch_file = os.path.join(slam_toolbox, 'launch', 'online_async_launch.py')
    slam_param_file = os.path.join(pkg_path, 'config',  'mapper_params_online_async.yaml')
    slam_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(slam_launch_file),
        launch_arguments={
            'params_file': slam_param_file,
            'use_sim_time': 'true', 
        }.items()
    )

    nav2_bringup = get_package_share_directory('nav2_bringup')
    nav2_launch_file = os.path.join(nav2_bringup, 'launch', 'navigation_launch.py')
    nav2_param_file = os.path.join(pkg_path, 'config', 'nav2_params.yaml')
    nav2_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(nav2_launch_file),
        launch_arguments={
            'use_sim_time': 'true',
            'params_file': nav2_param_file   # <--- Add this line!

        }.items(),
    )

    # this will run the explorer package to explore the environment autonomously
    explorer_package = Node (
        package='custom_explorer',
        executable='explorer',
        name='explorer',
        output='screen',
    )

    return LaunchDescription([

        rviz_node,
        slam_launch,
        nav2_launch,
        explorer_package,
    ])



