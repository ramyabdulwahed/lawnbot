import os

from ament_index_python.packages import get_package_share_directory


from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch.conditions import IfCondition, UnlessCondition
from launch.actions import IncludeLaunchDescription, TimerAction
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import Command
from launch.actions import RegisterEventHandler
from launch.event_handlers import OnProcessStart

from launch_ros.actions import Node
import xacro
from launch.actions import LogInfo
from launch.event_handlers import OnShutdown



def generate_launch_description():

    use_slam = LaunchConfiguration("use_slam")

    use_slam_arg = DeclareLaunchArgument(
        "use_slam",
        default_value="false"
    )

    pkg_path = get_package_share_directory('main_logic_controller')
    urdf_file = os.path.join(pkg_path, 'urdf', 'my_robot.urdf')
    yaml_file = os.path.join(pkg_path, 'config', 'my_controllers.yaml')

    map_path = os.path.join(pkg_path, 'config', 'bestsofar1240.yaml')



    # Load the URDF file using xacro
    xacro_file = os.path.join(pkg_path,'urdf','robot.urdf.xacro')
    robot_description_config = Command(['xacro ', xacro_file])
    params = {'robot_description': robot_description_config, 'use_sim_time': False}

     # Use Command to process the .xacro into URDF
    # doc = xacro.parse(open(urdf_file))
    # xacro.process_doc(doc)
    # robot_description = {'robot_description': doc.toxml()}

    robot_state_publisher_node = Node(
    package='robot_state_publisher',
    executable='robot_state_publisher',
    name='robot_state_publisher',
    output='screen',
    # parameters=[{'robot_description': open(urdf_file).read()}]
    #parameters=[robot_description,  {'use_sim_time': True}]
    parameters=[params]
    )

    ###### understand the commented modules below, to add them ####
    #    'cmd_vel_emulator =  main_logic_controller.cmd_vel_emulator:main',
    # 'sim_motor = main_logic_controller.SimMotorController:main',  ----------- no need for this its gazebo specific
    # 'odom_bridge = main_logic_controller.odom_bridge:main',     -------------- no need for this its gazebo specific
    # 'cmd_vel_bridge = main_logic_controller.cmd_vel_bridge:main',  -------------- no need for this its gazebo specific
    # 'odom_controller_testing = main_logic_controller.odom_controller_testing:main', 
    # 'exploration_monitor = main_logic_controller.exploration_monitor:main',

    #this node translates cmd_vel messages (from nav2) to messages that the kanga motor controller can understand
    # thus nav2 -> cmd_vel_emulator 
    Nav2_translator = Node (
        package='main_logic_controller',
        executable='cmd_vel_emulator',
        name='cmd_emulator',
        output='screen',
    )

    #laser node driver 
    sllidar_package = get_package_share_directory('sllidar_ros2')
    sllidar_launch_file = os.path.join(sllidar_package, 'launch', 'view_sllidar_a1_launch.py')
    laser_driver = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(sllidar_launch_file),
        launch_arguments={
            "frame_id": "laser_frame",
        }.items(),
    )

    #############################################################
    #this will run amcl and map_server to localize the robot in the environment
    #############################################################
    nav2 = get_package_share_directory('nav2_bringup')
    nav2_amcl_launch_file = os.path.join(nav2, 'launch', 'localization_launch.py')
    nav2_amcl = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(nav2_amcl_launch_file),
        launch_arguments={
            'use_sim_time': 'false',
            'map': map_path,
            'autostart': 'true'
        }.items(),
        #only run this if use_slam is false
        condition=UnlessCondition(use_slam)
    ) 


    #this will run nav2 to navigate the robot in the environment and to listen to the map
    nav2_launch_file = os.path.join(nav2, 'launch', 'navigation_launch.py')
    nav2_node_for_amcl = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(nav2_launch_file),
        launch_arguments={
            'use_sim_time':'false',
            #'params_file': map_path,
            'map_subscribe_transient_local': 'true',
        }.items(),
        condition=UnlessCondition(use_slam) #only run this if use_slam is false
    )
    ############################################################
    #slam_toolbox and nav2 and map_saver for exploration and mapping
    ############################################################
    slam_toolbox = get_package_share_directory('slam_toolbox')
    slam_launch_file = os.path.join(slam_toolbox, 'launch', 'online_async_launch.py')
    slam_param_file = os.path.join(pkg_path, 'config',  'mapper_params_online_async.yaml')
    slam_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(slam_launch_file),
        launch_arguments={
            'params_file': slam_param_file,
            'use_sim_time': 'false', 
        }.items(),
        condition=IfCondition(use_slam)  #only run this if use_slam is true
    ) 


    nav2_bringup = get_package_share_directory('nav2_bringup')
    nav2_launch_file = os.path.join(nav2_bringup, 'launch', 'navigation_launch.py')
    nav2_param_file = os.path.join(pkg_path, 'config', 'nav2_params.yaml')
    nav2_launch_for_slam = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(nav2_launch_file),
        launch_arguments={
            'use_sim_time': 'false',
            'params_file': nav2_param_file   # <--- Add this line!

        }.items(),
        condition=IfCondition(use_slam)  #only run this if use_slam is true
    )

    #map_saver_node is used to save the map after exploration is done
    #ros2 service call /map_saver/save_map nav2_msgs/srv/SaveMap "{name: 'bestmap'}"
    map_saver_node = Node(
        package="nav2_map_server",
        executable="map_saver_server",
        name="map_saver_server",
        output="screen",
        parameters=[
            {"use_sim_time": False},
            {"save_map_timeout": 5.0},
        ],
        condition=IfCondition(use_slam)
    )

    ############################################################
    #run teleop node for teleoperation of the robot - only for exploration (slam) mode
    ############################################################
    teleop_keyboard = Node(
        package="teleop_twist_keyboard",
        executable="teleop_twist_keyboard",
        name="teleop_twist_keyboard",
        output="screen",
        condition=IfCondition(use_slam),
    )


    ############################################################
    #run rviz2: note that config file is in the home directory
    ############################################################
    rviz_config_file = os.path.join(os.path.expanduser('~'), 'rvizConfig.rviz')
    rviz2 = Node(
    package='rviz2',
    executable='rviz2',
    name='rviz2',
    arguments=['-d', rviz_config_file],
    parameters=[{'use_sim_time': False}]  # Set use_sim_time to False for real robot operation
    )

    explorer_node = Node(
    package='custom_explorer',
    executable='explorer',
    name='explorer_node',
    output='screen',
    condition=IfCondition(use_slam),

    )


    main_logic_controller = Node(
        package='main_logic_controller',
        executable='main',
        name='main_logic_controller'
    )

    #this includes the odom publisher node, which publishes the odometry of the robot
    motor_controller = Node(
        package='main_logic_controller',
        executable='motor',
        name='motor_controller'
    )

    # path_publisher = Node(
    #     package='lawnbot_ros2',
    #     executable='path',
    #     name='path_publisher'
    # )

    light_controller = Node(
        package='main_logic_controller',
        executable='light',
        name='light_controller'
    )
    pump_controller = Node(
        package='main_logic_controller',
        executable='pump',
        name='pump_controller'
    )
    
    picamera_controller = Node(
        package='main_logic_controller',
        executable='picamera',
        name='picamera_controller'
    )
    object_detector = Node(
        package='main_logic_controller',
        executable='object_detector',
        name='object_detector'
    )
    vid_streamer = Node(
        package='main_logic_controller',
        executable='vid_streamer',
        name='vid_streamer'
    )
    start_stop = Node(
        package='main_logic_controller',
        executable='start_stop_wrapper',
        name='start_stop_wrapper'
    )

    # Handle Ctrl+C (SIGINT) for graceful shutdown
    handle_sigint = RegisterEventHandler(
        OnShutdown(
            on_shutdown=[LogInfo(msg="Caught Ctrl+C, shutting down lawnbot gracefully!")]
        )
    )

    return LaunchDescription([
        motor_controller,
        Nav2_translator,  #this is the node that translates cmd_vel messages to messages that the kanga motor controller can understand
        use_slam_arg,   #this is the argument to use slam or not
        #laser_driver, 
        nav2_amcl,  
        nav2_node_for_amcl,  #this is the node that runs amcl and map_server
        slam_launch,  
        nav2_launch_for_slam,  #this is the node that runs nav2 for slam
        robot_state_publisher_node,
        map_saver_node,  #this is the node that saves the map after exploration is done
#        laser_driver,  #this is the node that runs the laser driver
        #rviz2,  #this is the node that runs rviz2
        #teleop_keyboard, 

        #these are the low level controllers that control the robot
        #main_logic_controller,
        #motor_controller,
        #light_controller,
        #pump_controller,
        #picamera_controller,
        #object_detector,
        #vid_streamer,
        start_stop,
        handle_sigint,
        #explorer_node #this is the node that runs the explorer
    ])





