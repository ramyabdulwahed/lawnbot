# #!/bin/bash

# echo "🔧 Setting up ROS 2 Jazzy dependencies for Lawnbot..."

# # Source ROS Jazzy
# source /opt/ros/jazzy/setup.bash

# # Update and install core ROS tools
# sudo apt update
# sudo apt install -y \
#   python3-colcon-common-extensions \
#   python3-pip \
#   ros-jazzy-rclpy \
#   ros-jazzy-std-msgs \
#   ros-jazzy-geometry-msgs \
#   ros-jazzy-nav-msgs \
#   ros-jazzy-tf2-ros \
#   ros-jazzy-robot-state-publisher \
#   ros-jazzy-joint-state-publisher-gui \
#   ros-jazzy-rviz2 \
#   ros-jazzy-tf-transformations \
#   ros-jazzy-launch-ros \
#   ros-jazzy-ros2launch

# # Install Python packages (via pip)
# pip3 install serial numpy

# echo "✅ Done installing dependencies!"

#!/bin/bash

echo "🔧 Fixing GPG key and installing dependencies for ROS 2 Jazzy..."

# Update GPG key
sudo apt-key del F42ED6FBAB17C654 2>/dev/null
sudo curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | gpg --dearmor -o /usr/share/keyrings/ros-archive-keyring.gpg

# Re-add ROS sources with the new key
echo "deb [arch=arm64 signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(lsb_release -sc) main" | sudo tee /etc/apt/sources.list.d/ros2.list

# Update system and ROS repo
sudo apt update

# Install core ROS packages and tools
sudo apt install -y \
    python3-pip \
    python3-colcon-common-extensions \
    ros-jazzy-rclpy \
    ros-jazzy-std-msgs \
    ros-jazzy-geometry-msgs \
    ros-jazzy-nav-msgs \
    ros-jazzy-ros2launch \
    ros-jazzy-launch-ros \
    ros-jazzy-joint-state-publisher \
    ros-jazzy-joint-state-publisher-gui \
    ros-jazzy-rviz2 \
    ros-jazzy-robot-state-publisher \
    ros-jazzy-tf2-ros \
    ros-jazzy-tf-transformations

# Optional: Install Python packages globally (use only if you understand the risk)
pip3 install serial numpy --break-system-packages

echo "✅ All dependencies installed successfully!"
