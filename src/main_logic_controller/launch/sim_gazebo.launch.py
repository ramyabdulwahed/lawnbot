####### some notes ########
'''
IncludeLaunchDescription -  It tells ROS 2 to "run another launch file" inside my launch file.  
PythonLaunchDescriptionSource - It says "the other launch file is a Python launch file (.py)".
launch_arguments={ ... }.items() - It lets you pass launch arguments to the launch file you are including. It is like saying:
    ros2 launch online_async_launch.py params_file:=X use_sim_time:=Y
    But now you are doing this inside Python — giving it a dictionary of arguments:  
LaunchConfiguration('params_file') - It says "get the current value of the launch argument params_file".
.items() - This is just Python syntax → turns a dictionary into a list of key-value pairs. 
'''





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
    urdf_file = os.path.join(pkg_path, 'urdf', 'my_robot.urdf')
    yaml_file = os.path.join(pkg_path, 'config', 'my_controllers.yaml')


    # Load the URDF file using xacro
    xacro_file = os.path.join(pkg_path,'urdf','robot.urdf.xacro')
    robot_description_config = Command(['xacro ', xacro_file])
    params = {'robot_description': robot_description_config, 'use_sim_time': True}
     # Use Command to process the .xacro into URDF
    doc = xacro.parse(open(urdf_file))
    xacro.process_doc(doc)
    robot_description = {'robot_description': doc.toxml()}


    robot_state_publisher_node = Node(
    package='robot_state_publisher',
    executable='robot_state_publisher',
    name='robot_state_publisher',
    output='screen',
    # parameters=[{'robot_description': open(urdf_file).read()}]
    #parameters=[robot_description,  {'use_sim_time': True}]
    parameters=[params]
    )


    #simply starts Gazebo with its standard GUI and physics engine.
    gazebo_launch = IncludeLaunchDescription(
    PythonLaunchDescriptionSource(
        os.path.join(
            get_package_share_directory('gazebo_ros'),
            'launch',
            'gazebo.launch.py'
        )

    ),
    launch_arguments={
        #my world is located in the root dir ex. /home not the package dir
        'world': os.path.join( '/home','June10World.world'),  # Change this to your world file path
    }.items()
    
    )
    #ow that Gazebo is open, we want to spawn your robot model into the simulation
    #this node: Looks at the /robot_description parameter Spawns your robot into the world with the name my_robot
    spawn_entity = Node(
        package='gazebo_ros',
        executable='spawn_entity.py',
        arguments=[
             '-topic', 'robot_description',
            '-entity', 'my_robot',
            '-z', '0.0'  #  this adds the height offset
        ],
        parameters=[{'use_sim_time': True}],  
        output='screen'

    )

    #incase you face errors make sure to clean gazebo correctly by running the below:
    # pkill gzserver
    # pkill gzclient
    # pkill -9 gzserver
    # pkill -9 gzclient



    joint_state_broadcaster_spawner = Node(
        package='controller_manager',
        executable='spawner',
        arguments=['joint_broad', '--controller-manager-timeout', '50'],
        output='screen'
    )
# It’s launching this command behind the scenes: ros2 run controller_manager spawner.py left_track_velocity_controller --controller-manager-timeout 50 
    
    left_track_controller_spawner = Node(
        package='controller_manager',
        executable='spawner',
        # arguments=['track_velocity_controller', '--controller-manager-timeout', '50'],
        # arguments=['diff_cont', '--controller-manager-timeout', '50'],
        arguments=['diff_cont'],

        # remappings=[
        #     ("/diff_cont/odom", "/odom"),
        #     ("/diff_cont/cmd_vel_unstamped", "/cmd_vel")
        # ],

        output='screen',
        # parameters=[{
        # 'topic_command.unstamped': '/cmd_vel',
        # 'odom_topic': '/odom'
        # }]
    )

    odom_bridge = Node(
        package='main_logic_controller',
        executable='odom_bridge',
        name='odom_bridge',
        output='screen'
    )

    cmd_vel_bridge = Node(
        package='main_logic_controller',
        executable='cmd_vel_bridge',
        name='cmd_vel_bridge',
        output='screen'
    )

    # #this will launch rviz2 with a specific configuration file
    # rviz_config_file = os.path.join(pkg_path, 'config', '41xxRobotRviz.rviz')
    # rviz_node = Node (
    #     package='rviz2',
    #     executable='rviz2',
    #     name='rviz2',
    #     output='screen',
    #     arguments=['-d', rviz_config_file],
    #     parameters=[{'use_sim_time': True}]
    # )


    # slam_toolbox = get_package_share_directory('slam_toolbox')
    # slam_launch_file = os.path.join(slam_toolbox, 'launch', 'online_async_launch.py')
    # slam_param_file = os.path.join(pkg_path, 'config',  'mapper_params_online_async.yaml')
    # slam_launch = IncludeLaunchDescription(
    #     PythonLaunchDescriptionSource(slam_launch_file),
    #     launch_arguments={
    #         'params_file': slam_param_file,
    #         'use_sim_time': 'true', 
    #     }.items()
    # )

    # nav2_bringup = get_package_share_directory('nav2_bringup')
    # nav2_launch_file = os.path.join(nav2_bringup, 'launch', 'navigation_launch.py')
    # nav2_param_file = os.path.join(pkg_path, 'config', 'nav2_params.yaml')
    # nav2_launch = IncludeLaunchDescription(
    #     PythonLaunchDescriptionSource(nav2_launch_file),
    #     launch_arguments={
    #         'use_sim_time': 'true'
    #     }.items(),
    # )

    # #this will run the explorer package to explore the environment autonomously
    # explorer_package = Node (
    #     package='custom_explorer',
    #     executable='explorer',
    #     name='explorer',
    #     output='screen',
    # )

    







    # right_track_controller_spawner = Node(
    #     package='controller_manager',
    #     executable='spawner',
    #     arguments=['right_track_velocity_controller', '--controller-manager-timeout', '50'],
    #     output='screen'
    # )

    return LaunchDescription([
        robot_state_publisher_node,
        gazebo_launch,
        spawn_entity,
        joint_state_broadcaster_spawner,
        left_track_controller_spawner,
        #right_track_controller_spawner
        odom_bridge,
        cmd_vel_bridge,
        # rviz_node,
        # slam_launch,
        # nav2_launch,
        # explorer_package,
    ])


