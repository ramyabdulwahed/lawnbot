// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from main_controller_interfaces:msg/BoundingBox.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "main_controller_interfaces/msg/bounding_box.hpp"


#ifndef MAIN_CONTROLLER_INTERFACES__MSG__DETAIL__BOUNDING_BOX__BUILDER_HPP_
#define MAIN_CONTROLLER_INTERFACES__MSG__DETAIL__BOUNDING_BOX__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "main_controller_interfaces/msg/detail/bounding_box__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace main_controller_interfaces
{

namespace msg
{

namespace builder
{

class Init_BoundingBox_width
{
public:
  explicit Init_BoundingBox_width(::main_controller_interfaces::msg::BoundingBox & msg)
  : msg_(msg)
  {}
  ::main_controller_interfaces::msg::BoundingBox width(::main_controller_interfaces::msg::BoundingBox::_width_type arg)
  {
    msg_.width = std::move(arg);
    return std::move(msg_);
  }

private:
  ::main_controller_interfaces::msg::BoundingBox msg_;
};

class Init_BoundingBox_center_y
{
public:
  explicit Init_BoundingBox_center_y(::main_controller_interfaces::msg::BoundingBox & msg)
  : msg_(msg)
  {}
  Init_BoundingBox_width center_y(::main_controller_interfaces::msg::BoundingBox::_center_y_type arg)
  {
    msg_.center_y = std::move(arg);
    return Init_BoundingBox_width(msg_);
  }

private:
  ::main_controller_interfaces::msg::BoundingBox msg_;
};

class Init_BoundingBox_center_x
{
public:
  Init_BoundingBox_center_x()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_BoundingBox_center_y center_x(::main_controller_interfaces::msg::BoundingBox::_center_x_type arg)
  {
    msg_.center_x = std::move(arg);
    return Init_BoundingBox_center_y(msg_);
  }

private:
  ::main_controller_interfaces::msg::BoundingBox msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::main_controller_interfaces::msg::BoundingBox>()
{
  return main_controller_interfaces::msg::builder::Init_BoundingBox_center_x();
}

}  // namespace main_controller_interfaces

#endif  // MAIN_CONTROLLER_INTERFACES__MSG__DETAIL__BOUNDING_BOX__BUILDER_HPP_
