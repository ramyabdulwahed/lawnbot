// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from main_controller_interfaces:msg/BoundingBox.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "main_controller_interfaces/msg/bounding_box.hpp"


#ifndef MAIN_CONTROLLER_INTERFACES__MSG__DETAIL__BOUNDING_BOX__TRAITS_HPP_
#define MAIN_CONTROLLER_INTERFACES__MSG__DETAIL__BOUNDING_BOX__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "main_controller_interfaces/msg/detail/bounding_box__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace main_controller_interfaces
{

namespace msg
{

inline void to_flow_style_yaml(
  const BoundingBox & msg,
  std::ostream & out)
{
  out << "{";
  // member: center_x
  {
    out << "center_x: ";
    rosidl_generator_traits::value_to_yaml(msg.center_x, out);
    out << ", ";
  }

  // member: center_y
  {
    out << "center_y: ";
    rosidl_generator_traits::value_to_yaml(msg.center_y, out);
    out << ", ";
  }

  // member: width
  {
    out << "width: ";
    rosidl_generator_traits::value_to_yaml(msg.width, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const BoundingBox & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: center_x
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "center_x: ";
    rosidl_generator_traits::value_to_yaml(msg.center_x, out);
    out << "\n";
  }

  // member: center_y
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "center_y: ";
    rosidl_generator_traits::value_to_yaml(msg.center_y, out);
    out << "\n";
  }

  // member: width
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "width: ";
    rosidl_generator_traits::value_to_yaml(msg.width, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const BoundingBox & msg, bool use_flow_style = false)
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
  const main_controller_interfaces::msg::BoundingBox & msg,
  std::ostream & out, size_t indentation = 0)
{
  main_controller_interfaces::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use main_controller_interfaces::msg::to_yaml() instead")]]
inline std::string to_yaml(const main_controller_interfaces::msg::BoundingBox & msg)
{
  return main_controller_interfaces::msg::to_yaml(msg);
}

template<>
inline const char * data_type<main_controller_interfaces::msg::BoundingBox>()
{
  return "main_controller_interfaces::msg::BoundingBox";
}

template<>
inline const char * name<main_controller_interfaces::msg::BoundingBox>()
{
  return "main_controller_interfaces/msg/BoundingBox";
}

template<>
struct has_fixed_size<main_controller_interfaces::msg::BoundingBox>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<main_controller_interfaces::msg::BoundingBox>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<main_controller_interfaces::msg::BoundingBox>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // MAIN_CONTROLLER_INTERFACES__MSG__DETAIL__BOUNDING_BOX__TRAITS_HPP_
