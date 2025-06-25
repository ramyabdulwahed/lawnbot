from setuptools import find_packages, setup
from glob import glob

package_name = 'main_logic_controller'

setup(
    name=package_name,
    version='0.0.0',
    #packages=find_packages(exclude=['test']),
    packages=find_packages(include=['main_logic_controller', 'main_logic_controller.*']),

    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', glob('launch/*.py')),
        ('share/' + package_name + '/urdf', glob('urdf/*.*')),
        ('share/' + package_name + '/config', glob('config/*.*')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='ramy_abdulwahed',
    maintainer_email='rabdulwa@uoguelph.ca',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'main = main_logic_controller.41xx_main_logic_controller:main',
            'motor =  main_logic_controller.motor_controller:main',
            'path =  main_logic_controller.path_publisher:main',
            'light =  main_logic_controller.light_controller:main',
            'pump =  main_logic_controller.pump_controller:main',
            'picamera =  main_logic_controller.picamera_controller:main',
            'object_detector =  main_logic_controller.object_detector:main',
            'vid_streamer =  main_logic_controller.vid_streamer:main',
            'start_stop_wrapper =  main_logic_controller.start_stop_wrapper:main',
            'cmd_vel_emulator =  main_logic_controller.cmd_vel_emulator:main',
            #'sim_motor = main_logic_controller.SimMotorController:main',
            #'odom_bridge = main_logic_controller.odom_bridge:main',
            #'cmd_vel_bridge = main_logic_controller.cmd_vel_bridge:main',
            #'odom_controller_testing = main_logic_controller.odom_controller_testing:main',
            #'exploration_monitor = main_logic_controller.exploration_monitor:main',



        ],
    },
)
