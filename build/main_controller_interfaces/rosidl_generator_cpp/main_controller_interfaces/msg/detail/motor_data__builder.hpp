// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from main_controller_interfaces:msg/MotorData.idl
// generated code does not contain a copyright notice

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

class Init_MotorData_speed
{
public:
  explicit Init_MotorData_speed(::main_controller_interfaces::msg::MotorData & msg)
  : msg_(msg)
  {}
  ::main_controller_interfaces::msg::MotorData speed(::main_controller_interfaces::msg::MotorData::_speed_type arg)
  {
    msg_.speed = std::move(arg);
    return std::move(msg_);
  }

private:
  ::main_controller_interfaces::msg::MotorData msg_;
};

class Init_MotorData_position
{
public:
  explicit Init_MotorData_position(::main_controller_interfaces::msg::MotorData & msg)
  : msg_(msg)
  {}
  Init_MotorData_speed position(::main_controller_interfaces::msg::MotorData::_position_type arg)
  {
    msg_.position = std::move(arg);
    return Init_MotorData_speed(msg_);
  }

private:
  ::main_controller_interfaces::msg::MotorData msg_;
};

class Init_MotorData_op_code
{
public:
  Init_MotorData_op_code()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_MotorData_position op_code(::main_controller_interfaces::msg::MotorData::_op_code_type arg)
  {
    msg_.op_code = std::move(arg);
    return Init_MotorData_position(msg_);
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
  return main_controller_interfaces::msg::builder::Init_MotorData_op_code();
}

}  // namespace main_controller_interfaces

#endif  // MAIN_CONTROLLER_INTERFACES__MSG__DETAIL__MOTOR_DATA__BUILDER_HPP_
