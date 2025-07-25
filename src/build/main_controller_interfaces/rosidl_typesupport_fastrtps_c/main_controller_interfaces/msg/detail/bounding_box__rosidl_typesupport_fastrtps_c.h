// generated from rosidl_typesupport_fastrtps_c/resource/idl__rosidl_typesupport_fastrtps_c.h.em
// with input from main_controller_interfaces:msg/BoundingBox.idl
// generated code does not contain a copyright notice
#ifndef MAIN_CONTROLLER_INTERFACES__MSG__DETAIL__BOUNDING_BOX__ROSIDL_TYPESUPPORT_FASTRTPS_C_H_
#define MAIN_CONTROLLER_INTERFACES__MSG__DETAIL__BOUNDING_BOX__ROSIDL_TYPESUPPORT_FASTRTPS_C_H_


#include <stddef.h>
#include "rosidl_runtime_c/message_type_support_struct.h"
#include "rosidl_typesupport_interface/macros.h"
#include "main_controller_interfaces/msg/rosidl_typesupport_fastrtps_c__visibility_control.h"
#include "main_controller_interfaces/msg/detail/bounding_box__struct.h"
#include "fastcdr/Cdr.h"

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_main_controller_interfaces
bool cdr_serialize_main_controller_interfaces__msg__BoundingBox(
  const main_controller_interfaces__msg__BoundingBox * ros_message,
  eprosima::fastcdr::Cdr & cdr);

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_main_controller_interfaces
bool cdr_deserialize_main_controller_interfaces__msg__BoundingBox(
  eprosima::fastcdr::Cdr &,
  main_controller_interfaces__msg__BoundingBox * ros_message);

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_main_controller_interfaces
size_t get_serialized_size_main_controller_interfaces__msg__BoundingBox(
  const void * untyped_ros_message,
  size_t current_alignment);

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_main_controller_interfaces
size_t max_serialized_size_main_controller_interfaces__msg__BoundingBox(
  bool & full_bounded,
  bool & is_plain,
  size_t current_alignment);

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_main_controller_interfaces
bool cdr_serialize_key_main_controller_interfaces__msg__BoundingBox(
  const main_controller_interfaces__msg__BoundingBox * ros_message,
  eprosima::fastcdr::Cdr & cdr);

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_main_controller_interfaces
size_t get_serialized_size_key_main_controller_interfaces__msg__BoundingBox(
  const void * untyped_ros_message,
  size_t current_alignment);

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_main_controller_interfaces
size_t max_serialized_size_key_main_controller_interfaces__msg__BoundingBox(
  bool & full_bounded,
  bool & is_plain,
  size_t current_alignment);

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_main_controller_interfaces
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, main_controller_interfaces, msg, BoundingBox)();

#ifdef __cplusplus
}
#endif

#endif  // MAIN_CONTROLLER_INTERFACES__MSG__DETAIL__BOUNDING_BOX__ROSIDL_TYPESUPPORT_FASTRTPS_C_H_
