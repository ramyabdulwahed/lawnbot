// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from main_controller_interfaces:msg/MotorData.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "main_controller_interfaces/msg/motor_data.hpp"


#ifndef MAIN_CONTROLLER_INTERFACES__MSG__DETAIL__MOTOR_DATA__BUILDER_HPP_
#define MAIN_CONTROLLER_INTERFACES__MSG__DETAIL__MOTOR_DATA__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "main_controller_interfaces/msg/detail/motor_data__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace main_controller_interfaces
{

namespace msg
{

namespace builder
{

class Init_MotorData_right_speed
{
public:
  explicit Init_MotorData_right_speed(::main_controller_interfaces::msg::MotorData & msg)
  : msg_(msg)
  {}
  ::main_controller_interfaces::msg::MotorData right_speed(::main_controller_interfaces::msg::MotorData::_right_speed_type arg)
  {
    msg_.right_speed = std::move(arg);
    return std::move(msg_);
  }

private:
  ::main_controller_interfaces::msg::MotorData msg_;
};

class Init_MotorData_left_speed
{
public:
  Init_MotorData_left_speed()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_MotorData_right_speed left_speed(::main_controller_interfaces::msg::MotorData::_left_speed_type arg)
  {
    msg_.left_speed = std::move(arg);
    return Init_MotorData_right_speed(msg_);
  }

private:
  ::main_controller_interfaces::msg::MotorData msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::main_controller_interfaces::msg::MotorData>()
{
  return main_controller_interfaces::msg::builder::Init_MotorData_left_speed();
}

}  // namespace main_controller_interfaces

#endif  // MAIN_CONTROLLER_INTERFACES__MSG__DETAIL__MOTOR_DATA__BUILDER_HPP_
