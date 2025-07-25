import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/lawnbot/ROS2/lawnbot/src/install/custom_explorer'
