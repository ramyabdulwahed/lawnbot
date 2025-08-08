# lawnbot

## 🛠 How to Run

1. Clone and navigate to the repository:
   cd ~/lawnbot

2. Build the workspace:
   colcon build --symlink-install

3. Source the setup file:
   source install/setup.bash

---

## 🚀 Launching the Robot

Step 1 — Run the LiDAR driver:
   ros2 launch sllidar_ros2 view_sllidar_a1_launch.py frame_id:=laser_frame

Step 2 — Start in SLAM mode (mapping & exploration):
   ros2 launch main_logic_controller launch_robot.launch.py use_slam:=true

Step 3 — Run the autonomous explorer:
   ros2 run custom_explorer explorer

---

## 🛑 Emergency Stop
If the robot crashes or behaves unexpectedly:
   ros2 service call /motor_stop std_srvs/srv/Empty {}

---

## 💾 Saving the Map
After the explorer finishes (e.g., logs show "no valid frontiers"), save the map:
   ros2 run nav2_map_server map_saver_cli -f <map_name>

---

## 📌 Notes
- Make sure all dependencies are installed before running.
- Replace <map_name> with your preferred filename when saving the map.
- Use --symlink-install during build for faster development iterations.
