#!/bin/bash

echo "🔧 Setting up ROS 2 Jazzy dependencies for Lawnbot..."

# Source ROS Jazzy
source /opt/ros/jazzy/setup.bash

# Update and install core ROS tools
sudo apt update
sudo apt install -y \
  python3-colcon-common-extensions \
  python3-pip \
  ros-jazzy-rclpy \
  ros-jazzy-std-msgs \
  ros-jazzy-geometry-msgs \
  ros-jazzy-nav-msgs \
  ros-jazzy-tf2-ros \
  ros-jazzy-robot-state-publisher \
  ros-jazzy-joint-state-publisher-gui \
  ros-jazzy-rviz2 \
  ros-jazzy-tf-transformations \
  ros-jazzy-launch-ros \
  ros-jazzy-ros2launch

# Install Python packages (via pip)
pip3 install serial numpy

echo "✅ Done installing dependencies!"
