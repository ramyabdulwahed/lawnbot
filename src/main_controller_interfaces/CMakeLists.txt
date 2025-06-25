cmake_minimum_required(VERSION 3.5)
project(main_controller_interfaces)

find_package(ament_cmake REQUIRED)
find_package(rosidl_default_generators REQUIRED)

rosidl_generate_interfaces(${PROJECT_NAME}
  "msg/MotorData.msg"
)


ament_package()
