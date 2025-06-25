// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from main_controller_interfaces:msg/MotorData.idl
// generated code does not contain a copyright notice

#ifndef MAIN_CONTROLLER_INTERFACES__MSG__DETAIL__MOTOR_DATA__TRAITS_HPP_
#define MAIN_CONTROLLER_INTERFACES__MSG__DETAIL__MOTOR_DATA__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "main_controller_interfaces/msg/detail/motor_data__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace main_controller_interfaces
{

namespace msg
{

inline void to_flow_style_yaml(
  const MotorData & msg,
  std::ostream & out)
{
  out << "{";
  // member: op_code
  {
    out << "op_code: ";
    rosidl_generator_traits::value_to_yaml(msg.op_code, out);
    out << ", ";
  }

  // member: position
  {
    out << "position: ";
    rosidl_generator_traits::value_to_yaml(msg.position, out);
    out << ", ";
  }

  // member: speed
  {
    out << "speed: ";
    rosidl_generator_traits::value_to_yaml(msg.speed, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const MotorData & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: op_code
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "op_code: ";
    rosidl_generator_traits::value_to_yaml(msg.op_code, out);
    out << "\n";
  }

  // member: position
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "position: ";
    rosidl_generator_traits::value_to_yaml(msg.position, out);
    out << "\n";
  }

  // member: speed
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "speed: ";
    rosidl_generator_traits::value_to_yaml(msg.speed, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const MotorData & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace msg

}  // namespace main_controller_interfaces

namespace rosidl_generator_traits
{

[[deprecated("use main_controller_interfaces::msg::to_block_style_yaml() instead")]]
inline void to_yaml(
  const main_controller_interfaces::msg::MotorData & msg,
  std::ostream & out, size_t indentation = 0)
{
  main_controller_interfaces::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use main_controller_interfaces::msg::to_yaml() instead")]]
inline std::string to_yaml(const main_controller_interfaces::msg::MotorData & msg)
{
  return main_controller_interfaces::msg::to_yaml(msg);
}

template<>
inline const char * data_type<main_controller_interfaces::msg::MotorData>()
{
  return "main_controller_interfaces::msg::MotorData";
}

template<>
inline const char * name<main_controller_interfaces::msg::MotorData>()
{
  return "main_controller_interfaces/msg/MotorData";
}

template<>
struct has_fixed_size<main_controller_interfaces::msg::MotorData>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<main_controller_interfaces::msg::MotorData>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<main_controller_interfaces::msg::MotorData>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // MAIN_CONTROLLER_INTERFACES__MSG__DETAIL__MOTOR_DATA__TRAITS_HPP_
