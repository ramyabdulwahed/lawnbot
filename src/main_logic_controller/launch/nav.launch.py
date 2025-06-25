#as we run this file, the base map wont be changed since we are not running the slam_toolbox, but
# the cost map gets updated as the robot moves and explores the environment


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

    lifecycle_nodes = ["map_server"]

    #map_path = os.path.join(pkg_path, 'config', 'bestsofar1240.yaml')
    map_path = os.path.join(pkg_path, 'config', 'mymap11.yaml')
    nav2_map_server = Node(
    package="nav2_map_server",
    executable="map_server",
    name="map_server",
    output="screen",
    parameters=[
        {"yaml_filename": map_path},
        {"use_sim_time": True},
    ],
    )

    nav2_lifecycle_manager = Node(
        package="nav2_lifecycle_manager",
        executable="lifecycle_manager",
        name="lifecycle_manager_localization",
        output="screen",
        parameters=[
            {"node_names": lifecycle_nodes},
            {"use_sim_time": 'true'},
            {"autostart": 'rrue'}
        ],
    )
    #this will run amcl and map_server to localize the robot in the environment
    nav2 = get_package_share_directory('nav2_bringup')
    nav2_amcl_launch_file = os.path.join(nav2, 'launch', 'localization_launch.py')
    nac2_amcl = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(nav2_amcl_launch_file),
        launch_arguments={
            'use_sim_time':'true',
            'map': map_path,
            'autostart': 'true'

                          }.items())
    
    #this will run nav2 to navigate the robot in the environment and to listen to the map
    nav2_launch_file = os.path.join(nav2, 'launch', 'navigation_launch.py')
    nav2 = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(nav2_launch_file),
        launch_arguments={
            'use_sim_time':'true',
            #'params_file': map_path,
            'map_subscribe_transient_local': 'true',
                          }.items())
    
    rviz_config_file = os.path.join(os.path.expanduser('~'), 'rvizConfig.rviz')
    rviz2 = Node(
    package='rviz2',
    executable='rviz2',
    name='rviz2',
    arguments=['-d', rviz_config_file],
    parameters=[{'use_sim_time': True}]
)

    return LaunchDescription([
        #nav2_map_server,
        #nav2_lifecycle_manager,
        nac2_amcl,
        nav2,
        rviz2,
     ])