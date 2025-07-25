// generated from rosidl_typesupport_introspection_cpp/resource/idl__type_support.cpp.em
// with input from main_controller_interfaces:msg/BoundingBox.idl
// generated code does not contain a copyright notice

#include "array"
#include "cstddef"
#include "string"
#include "vector"
#include "rosidl_runtime_c/message_type_support_struct.h"
#include "rosidl_typesupport_cpp/message_type_support.hpp"
#include "rosidl_typesupport_interface/macros.h"
#include "main_controller_interfaces/msg/detail/bounding_box__functions.h"
#include "main_controller_interfaces/msg/detail/bounding_box__struct.hpp"
#include "rosidl_typesupport_introspection_cpp/field_types.hpp"
#include "rosidl_typesupport_introspection_cpp/identifier.hpp"
#include "rosidl_typesupport_introspection_cpp/message_introspection.hpp"
#include "rosidl_typesupport_introspection_cpp/message_type_support_decl.hpp"
#include "rosidl_typesupport_introspection_cpp/visibility_control.h"

namespace main_controller_interfaces
{

namespace msg
{

namespace rosidl_typesupport_introspection_cpp
{

void BoundingBox_init_function(
  void * message_memory, rosidl_runtime_cpp::MessageInitialization _init)
{
  new (message_memory) main_controller_interfaces::msg::BoundingBox(_init);
}

void BoundingBox_fini_function(void * message_memory)
{
  auto typed_message = static_cast<main_controller_interfaces::msg::BoundingBox *>(message_memory);
  typed_message->~BoundingBox();
}

static const ::rosidl_typesupport_introspection_cpp::MessageMember BoundingBox_message_member_array[3] = {
  {
    "center_x",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    false,  // is key
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(main_controller_interfaces::msg::BoundingBox, center_x),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr,  // fetch(index, &value) function pointer
    nullptr,  // assign(index, value) function pointer
    nullptr  // resize(index) function pointer
  },
  {
    "center_y",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    false,  // is key
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(main_controller_interfaces::msg::BoundingBox, center_y),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr,  // fetch(index, &value) function pointer
    nullptr,  // assign(index, value) function pointer
    nullptr  // resize(index) function pointer
  },
  {
    "width",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    false,  // is key
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(main_controller_interfaces::msg::BoundingBox, width),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr,  // fetch(index, &value) function pointer
    nullptr,  // assign(index, value) function pointer
    nullptr  // resize(index) function pointer
  }
};

static const ::rosidl_typesupport_introspection_cpp::MessageMembers BoundingBox_message_members = {
  "main_controller_interfaces::msg",  // message namespace
  "BoundingBox",  // message name
  3,  // number of fields
  sizeof(main_controller_interfaces::msg::BoundingBox),
  false,  // has_any_key_member_
  BoundingBox_message_member_array,  // message members
  BoundingBox_init_function,  // function to initialize message memory (memory has to be allocated)
  BoundingBox_fini_function  // function to terminate message instance (will not free memory)
};

static const rosidl_message_type_support_t BoundingBox_message_type_support_handle = {
  ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  &BoundingBox_message_members,
  get_message_typesupport_handle_function,
  &main_controller_interfaces__msg__BoundingBox__get_type_hash,
  &main_controller_interfaces__msg__BoundingBox__get_type_description,
  &main_controller_interfaces__msg__BoundingBox__get_type_description_sources,
};

}  // namespace rosidl_typesupport_introspection_cpp

}  // namespace msg

}  // namespace main_controller_interfaces


namespace rosidl_typesupport_introspection_cpp
{

template<>
ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
get_message_type_support_handle<main_controller_interfaces::msg::BoundingBox>()
{
  return &::main_controller_interfaces::msg::rosidl_typesupport_introspection_cpp::BoundingBox_message_type_support_handle;
}

}  // namespace rosidl_typesupport_introspection_cpp

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, main_controller_interfaces, msg, BoundingBox)() {
  return &::main_controller_interfaces::msg::rosidl_typesupport_introspection_cpp::BoundingBox_message_type_support_handle;
}

#ifdef __cplusplus
}
#endif
